from core.cognition import Cognition
from core.game import GamePlay
from core.robot_control import RobotControl
from core.serverintegrate import ServerIntegrate


class Main:
    def __init__(self):
        self.server = ServerIntegrate()
        self.robot_control = RobotControl()
        self.cognition = Cognition()
        self.game = GamePlay(self.robot_control, self.cognition, self.server)

    def run(self):
        self.server.create_new_game()
        print('Game code:', self.server.code)
        self.game.play()


if __name__ == '__main__':
    Main().run()
