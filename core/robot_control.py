import Arm_Lib
import json
import time


class RobotControl:
    def __init__(self):
        self.coordinates = json.load(open('coordinates.json'))
        self.standby_number = 1
        self.robot = Arm_Lib.Arm_Device()
        pass

    def move(self, number: int):
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 0, 600)
        time.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 180, 600)
        time.sleep(0.6)
        self.robot.Arm_serial_servo_write6(90, 90, 90, 90, 90, 180, 600)
        time.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 180, 600)
        time.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 0, 600)
        time.sleep(0.6)
        self.robot.Arm_serial_servo_write6(90, 90, 90, 90, 90, 0, 600)
        time.sleep(0.6)
        self.standby_number += 1
        return 


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # control = RobotControl()
    # loop.run_until_complete(asyncio.wait([control.move(1)]))
    pass
