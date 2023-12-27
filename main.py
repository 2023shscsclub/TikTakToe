from core.cognition import Cognition
from core.game import GamePlay
from core.robot_control import RobotControl
from core.serverintegrate import ServerIntegrate
import time


class Main:
    def __init__(self):
        self.server = ServerIntegrate(self)
        self.robot_control = RobotControl()
        self.cognition = Cognition()
        self.game = GamePlay(self)

    def run(self):
        self.server.create_new_game()
        print('Game code:', self.server.code)
        while True:
            if self.server.check_nick():
                break
            time.sleep(3)
        self.game.play()
        self.server.update_game("None")
        self.server.end_game()


if __name__ == '__main__':
    Main().run()
