import requests
import random


class ServerIntegrate:
    def __init__(self, main):
        self.game = main.game
        self.URL = "https://mbp16.ez0.us/csclub/tiktaktoe?data=all"
        self.code = None

    def get_previous_game(self):
        return requests.get(self.URL).json()

    def create_new_game(self):
        while self.code is None or self.code in [game["code"] for game in self.get_previous_game()]:
            self.code = random.randint(100000, 999999)
        requests.post(self.URL, json={"code": self.code, "board": [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]})
        return

    def update_game(self):
        requests.put(self.URL, json={"code": self.code, "board": self.game.board, "winner": self.game.winner})
        return

    def end_game(self):
        requests.delete(self.URL, json={"code": self.code})
        return

    def check_nick(self):
        return requests.get(f"https://mbp16.ez0.us/csclub/tiktaktoe?data=only&code={self.code}")["nickname"] is not None
