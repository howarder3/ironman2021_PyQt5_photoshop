from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QSlider

from opencv_engine import opencv_engine

# videoplayer_state_dict = {
#  "stop":0,   
#  "play":1,
#  "pause":2     
# }

class video_controller(object):
    def __init__(self, video_path, ui):
        self.video_path = video_path
        self.ui = ui
        self.list_collect_points = []
        self.qpixmap_fix_width = 800 # 16x9 = 1920x1080 = 1280x720 = 800x450
        self.qpixmap_fix_height = 450
        self.current_frame_no = 0
        self.videoplayer_state = "pause"
        self.init_video_info()
        self.set_video_player()

    def init_video_info(self):
        videoinfo = opencv_engine.getvideoinfo(self.video_path)
        self.vc = videoinfo["vc"]
        self.video_fps = videoinfo["fps"]
        self.video_total_frame_count = videoinfo["frame_count"]
        self.video_width = videoinfo["width"]
        self.video_height = videoinfo["height"]

        self.ui.slider_videoframe.setRange(0, self.video_total_frame_count-1)
        self.ui.slider_videoframe.valueChanged.connect(self.getslidervalue)

    def set_video_player(self):
        self.timer=QTimer() # init QTimer
        self.timer.timeout.connect(self.timer_timeout_job) # when timeout, do run one
        # self.timer.start(1000//self.video_fps) # start Timer, here we set '1000ms//Nfps' while timeout one time
        self.timer.start(1) # but if CPU can not decode as fast as fps, we set 1 (need decode time)
        self.ui.label_videoframe.mousePressEvent = self.mouse_press_event # set_clicked_position
        self.ui.button_clear_points.clicked.connect(self.clear_points)
        self.ui.button_generate_rois.clicked.connect(self.generate_rois)

    def __get_frame_from_frame_no(self, frame_no):
        self.vc.set(1, frame_no)
        ret, frame = self.vc.read()
        self.ui.label_framecnt.setText(f"frame number: {frame_no}/{self.video_total_frame_count-1}")
        self.setslidervalue(frame_no)
        return frame

    def __update_label_frame(self, frame):
        bytesPerline = 3 * self.video_width
        frame = self.__update_points_onscreen(frame)
        qimg = QImage(frame, self.video_width, self.video_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)

        if self.qpixmap.width()/16 >= self.qpixmap.height()/9: # like 1600/16 > 90/9, height is shorter, align width
            self.qpixmap = self.qpixmap.scaledToWidth(self.qpixmap_fix_width)
        else: # like 1600/16 < 9000/9, width is shorter, align height
            self.qpixmap = self.qpixmap.scaledToHeight(self.qpixmap_fix_height)
        self.ui.label_videoframe.setPixmap(self.qpixmap)
        # self.ui.label_videoframe.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop) # up and left
        self.ui.label_videoframe.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # Center


    def play(self):
        self.videoplayer_state = "play"

    def stop(self):
        self.videoplayer_state = "stop"

    def pause(self):
        self.videoplayer_state = "pause"

    def timer_timeout_job(self):
        frame = self.__get_frame_from_frame_no(self.current_frame_no)
        self.__update_label_frame(frame)

        if (self.videoplayer_state == "play"):
            if self.current_frame_no >= self.video_total_frame_count-1:
                self.videoplayer_state = "pause"
            else:
                self.current_frame_no += 1

        if (self.videoplayer_state == "stop"):
            self.current_frame_no = 0

        if (self.videoplayer_state == "pause"):
            self.current_frame_no = self.current_frame_no

    def getslidervalue(self):
        self.current_frame_no = self.ui.slider_videoframe.value()

    def setslidervalue(self, value):
        self.ui.slider_videoframe.setValue(self.current_frame_no)

    def mouse_press_event(self, event):
        print(f"[show_mouse_press] {event.x()=}, {event.y()=}, {event.button()=}")
        norm_x = event.x()/self.qpixmap.width()
        norm_y = event.y()/self.qpixmap.height()
        if event.button() == 2: # right clicked
            self.list_collect_points.append(self.list_collect_points[0])
            self.__update_text_show_points()

        elif event.button() == 1: # left clicked
            self.list_collect_points.append((norm_x, norm_y))
            self.__update_text_show_points()

    def __update_text_show_points(self):
        msg = "Current points (right click to return origin):\n"
        for ele in self.list_collect_points:
            msg += f"({ele[0]},{ele[1]})\n"
        self.ui.text_save_points.setText(msg)

    def clear_points(self):
        self.list_collect_points = []
        self.__update_text_show_points()

    def generate_rois(self):
        msg = "[\n"
        for ele in self.list_collect_points:
            msg += f"[{ele[0]},{ele[1]}],\n"
        msg += "]"
        self.ui.text_output_rois.setText(msg)

    def __update_points_onscreen(self, frame):
        if len(self.list_collect_points) == 0:
            pass
        else: # len(list) >= 1
            # first points
            frame = opencv_engine.draw_point(frame, point=self.list_collect_points[0], color = (0, 0, 255)) # red
            # if len = 1, no lines
            for idx in range(1, len(self.list_collect_points)):
                frame = opencv_engine.draw_point(frame, point=self.list_collect_points[idx], color = (0, 0, 255)) # red
                frame = opencv_engine.draw_line(frame, start_point =self.list_collect_points[idx-1], end_point=self.list_collect_points[idx], color = (0, 255, 0)) # green

        return frame



