from core.cognition import Cognition
from core.game import GamePlay
from core.robot_control import RobotControl


class Main:
    def __init__(self):
        robot_control = RobotControl()
        game = GamePlay(robot_control)
        cognition = Cognition(game)
        self.run()

    def run(self):
        pass


if __name__ == '__main__':
    Main()
