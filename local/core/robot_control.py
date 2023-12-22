import Arm_Lib
import json
import asyncio


class RobotControl:
    def __init__(self):
        self.coordinates = json.load(open('local/coordinates.json'))
        self.standby_number = 1
        self.robot = Arm_Lib.Arm_Device()
        pass

    async def move(self, number: int):
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 180, 600)
        await asyncio.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["standby" + str(self.standby_number)], 0, 600)
        await asyncio.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 0, 600)
        await asyncio.sleep(0.6)
        self.robot.Arm_serial_servo_write6(*self.coordinates["board" + str(number)], 180, 600)
        await asyncio.sleep(0.6)
        self.robot.Arm_serial_servo_write6(90, 90, 90, 90, 90, 0, 600)
        await asyncio.sleep(0.6)
        self.standby_number += 1


if __name__ == '__main__':
    control = RobotControl()
    control.move(1)
