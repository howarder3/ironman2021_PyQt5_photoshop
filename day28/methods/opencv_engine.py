import cv2
import numpy as np

from utils import WongWongLogger, WongWongDebugger, WongWongTimer
logger = WongWongLogger()

class opencv_engine(object):

    @staticmethod
    def point_float_to_int(point):
        return (int(point[0]), int(point[1]))

    @staticmethod
    def read_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def draw_point(img, point=(0, 0), color = (0, 0, 255)): # red
        point = opencv_engine.point_float_to_int(point)
        print(f"get {point=}")
        point_size = 1
        thickness = 4
        return cv2.circle(img, point, point_size, color, thickness)

    @staticmethod
    def draw_line(img, start_point = (0, 0), end_point = (0, 0), color = (0, 255, 0)): # green
        start_point = opencv_engine.point_float_to_int(start_point)
        end_point = opencv_engine.point_float_to_int(end_point)
        thickness = 3 # width
        return cv2.line(img, start_point, end_point, color, thickness)

    @staticmethod
    def draw_rectangle_by_points(img, left_up=(0, 0), right_down=(0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.point_float_to_int(left_up)
        right_down = opencv_engine.point_float_to_int(right_down)
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)

    @staticmethod
    def draw_rectangle_by_xywh(img, xywh=(0, 0, 0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.point_float_to_int((xywh[0], xywh[1]))
        right_down = opencv_engine.point_float_to_int((xywh[0]+xywh[2], xywh[1]+xywh[3]))
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)

    @staticmethod    
    def modify_lightness_saturation(img, lightness = 0, saturation = 0): # range: -100 ~ 100
        logger.info(f"get lightness = {lightness}, saturation = {saturation}")
        if lightness == 0 and saturation == 0: # no change
            return img
        # lightness 調整為  "1 +/- 幾 %"
        # saturation 調整為 "1 +/- 幾 %"
        origin_img = img

        # 圖像歸一化，且轉換為浮點型
        fImg = img.astype(np.float32)
        fImg = fImg / 255.0
        
        # 顏色空間轉換 BGR -> HLS
        hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
        hlsCopy = np.copy(hlsImg)
    
        # 亮度調整
        hlsCopy[:, :, 1] = (1 + lightness / 100.0) * hlsCopy[:, :, 1]
        hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1

        # 飽和度調整
        hlsCopy[:, :, 2] = (1 + saturation / 100.0) * hlsCopy[:, :, 2]
        hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1
        
        # 顏色空間反轉換 HLS -> BGR 
        result_img = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
        result_img = ((result_img * 255).astype(np.uint8))


        return result_img

    