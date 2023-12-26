import requests
import random


class ServerIntegrate:
    def __init__(self):
        self.URL = "https://mbp16.ez0.us/csclub/tiktaktoe/"
        self.code = None

    def get_previous_game(self):
        return requests.get(self.URL).json()

    def create_new_game(self):
        while self.code is None or self.code in [game["code"] for game in self.get_previous_game()]:
            self.code = random.randint(100000, 999999)
        requests.post(self.URL, json={"code": self.code, "board": [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]})
        return

    def update_game(self, board):
        requests.put(self.URL, json={"code": self.code, "board": board})
        return

    def end_game(self):
        requests.delete(self.URL, json={"code": self.code})
        return
