import cv2

class opencv_engine(object):
    @staticmethod
    def norm_point_to_int(img, point):
        img_height, img_width, img_channel = img.shape
        return (int(img_width*point[0]), int(img_height*point[1]))

    @staticmethod
    def read_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def draw_point(img, point=(0, 0), color = (0, 0, 255)): # red
        point = opencv_engine.norm_point_to_int(img, point)
        # print(f"get {point=}")
        point_size = 10
        thickness = 4
        return cv2.circle(img, point, point_size, color, thickness)

    @staticmethod
    def draw_line(img, start_point = (0, 0), end_point = (0, 0), color = (0, 255, 0)): # green
        start_point = opencv_engine.norm_point_to_int(img, start_point)
        end_point = opencv_engine.norm_point_to_int(img, end_point)
        thickness = 3 # width
        return cv2.line(img, start_point, end_point, color, thickness)

    @staticmethod
    def draw_rectangle_by_points(img, left_up=(0, 0), right_down=(0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.norm_point_to_int(img, left_up)
        right_down = opencv_engine.norm_point_to_int(img, right_down)
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)

    @staticmethod
    def draw_rectangle_by_xywh(img, xywh=(0, 0, 0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.norm_point_to_int(img, (xywh[0], xywh[1]))
        right_down = opencv_engine.norm_point_to_int(img, (xywh[0]+xywh[2], xywh[1]+xywh[3]))
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)

    @staticmethod
    def getvideoinfo(video_path): 
        # https://docs.opencv.org/4.5.3/dc/d3d/videoio_8hpp.html
        videoinfo = {}
        vc = cv2.VideoCapture(video_path)
        videoinfo["vc"] = vc
        videoinfo["fps"] = vc.get(cv2.CAP_PROP_FPS)
        videoinfo["frame_count"] = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
        videoinfo["width"] = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
        videoinfo["height"] = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return videoinfo
        