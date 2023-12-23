from core.cognition import Cognition
from core.game import GamePlay
from core.robot_control import RobotControl
import asyncio


class Main:
    def __init__(self):
        self.robot_control = RobotControl()
        self.cognition = Cognition()
        self.game = GamePlay(self.robot_control, self.cognition)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([self.game.play()]))


if __name__ == '__main__':
    Main().run()
