from core.cognition import Cognition
from core.game import GamePlay
from core.robot_control import RobotControl


class Main:
    def __init__(self):
        game = GamePlay()
        cognition = Cognition()
        robot_control = RobotControl()


if __name__ == '__main__':
    Main()