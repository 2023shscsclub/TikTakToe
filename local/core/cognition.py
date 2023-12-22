import numpy as np
import cv2
import asyncio


class Cognition:
    def __init__(self, game):
        self.game = game
        self.camera = cv2.VideoCapture(0)
        self.camera_rgb = np.ndarray(shape=(480, 640, 3), dtype=np.uint8)

    async def get_image(self):
        while True:
            ret, frame = self.camera.read()
            self.camera_rgb = frame
            await asyncio.sleep(0.1)

    def get_coordinates(self):
        hsv = cv2.cvtColor(self.camera_rgb, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 0])
        upper = np.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(self.camera_rgb, self.camera_rgb, mask=mask)
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        coordinates = []
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                M = cv2.moments(contour)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                coordinates.append((cx, cy))
        return coordinates

    @staticmethod
    def location_on_board(coordinate):
        if coordinate[0] < 213:
            if coordinate[1] < 160:
                return 1
            elif coordinate[1] < 320:
                return 4
            else:
                return 7
        elif coordinate[0] < 426:
            if coordinate[1] < 160:
                return 2
            elif coordinate[1] < 320:
                return 5
            else:
                return 8
        else:
            if coordinate[1] < 160:
                return 3
            elif coordinate[1] < 320:
                return 6
            else:
                return 9

    def locations_on_board(self):
        coordinates = self.get_coordinates()
        locations = []
        for coordinate in coordinates:
            locations.append(self.location_on_board(coordinate))
        return locations
