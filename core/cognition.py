import numpy as np
import cv2


class Cognition:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.camera_rgb = np.ndarray(shape=(480, 640, 3), dtype=np.uint8)
        self.player_locations = []

    def get_image(self):
        _, frame = self.camera.read()
        self.camera_rgb = frame

    def get_coordinates(self):
        coordinates = []
        hsv = cv2.cvtColor(self.camera_rgb, cv2.COLOR_BGR2HSV)
        red_lower = np.array([0, 100, 100])
        red_upper = np.array([10, 255, 255])
        red_mask = cv2.inRange(hsv, red_lower, red_upper)
        red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in red_contours:
            if cv2.contourArea(contour) > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                coordinates.append((x + w // 2, y + h // 2))
        return coordinates

    @staticmethod
    def location_on_board(coordinate):
        if 880<= coordinate[0] < 1220:
            if 40 <= coordinate[1] < 320:
                return 1
            elif 320 <= coordinate[1] < 590:
                return 4
            elif 590 <= coordinate[1] < 860:
                return 7
        elif 1220 <= coordinate[0] < 1540:
            if 40<= coordinate[1] < 320:
                return 2
            elif 320 <= coordinate[1] < 590:
                return 5
            elif 590 <= coordinate[1] < 860:
                return 8
        elif 1540 <= coordinate[0] < 1850:
            if 40 <= coordinate[1] < 320:
                return 3
            elif 320 <= coordinate[1] < 590:
                return 6
            elif 590 <= coordinate[1] < 860:
                return 9

    def get_locations_on_board(self):
        self.get_image()
        coordinates = self.get_coordinates()
        self.player_locations = []
        for coordinate in coordinates:
            self.player_locations.append(self.location_on_board(coordinate))
        self.player_locations = list(set(self.player_locations))
