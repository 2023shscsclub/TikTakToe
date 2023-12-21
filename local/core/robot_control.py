import Arm_Lib
import json


class RobotControl:
    def __init__(self):
        self.coordinates = json.load(open('../coordinates.json'))
        self.standby_number = 1
        self.robot = Arm_Lib.Arm_Device()
        pass

    def move(self, number: int):
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 180, 600)
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 0, 600)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 0, 600)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 180, 600)
        self.robot.Arm_serial_servo_write6(90, 90, 90, 90, 90, 0, 600)
        self.standby_number += 1
        pass
