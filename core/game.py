import random
import time


class GamePlay:
    def __init__(self, main):
        self.robot_control = main.robot_control
        self.cognition = main.cognition
        self.server = main.server
        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def print_board(self):
        for i in range(3):
            print(*self.board[i])
        print()

    def player_move_cognition(self):
        current_locations = []
        target = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "O":
                    current_locations.append(i*3+j+1)
        while True:
            self.cognition.get_locations_on_board()
            while True:
                if len(self.cognition.player_locations) > len(current_locations):
                    time.sleep(3)
                    if len(self.cognition.player_locations) > len(current_locations):
                        break
            for location in self.cognition.player_locations:
                if location in current_locations:
                    continue
                else:
                    target = location
            if self.player_move(*divmod(target - 1, 3)):
                break

    def player_move(self, row: int, col: int):
        if row not in range(3) or col not in range(3):
            print('That space is not in the board')
            return False
        if self.board[row][col] != '_':
            print('It`s already taken')
            return False
        self.board[row][col] = 'O'
        self.check_winner()
        self.server.update_game("computer")
        return True

    def computer_move(self):
        move = self.find_possible_wins()
        if move:
            for i in move:
                if i[2] == "X":
                    self.board[i[0]][i[1]] = 'X'
                    self.check_winner()
                    self.server.update_game("player")
                    self.robot_control.move(i[0] * 3 + i[1] + 1)
                    return
            move = random.choice(move)
            if random.randint(0, 9) != 0:
                self.board[move[0]][move[1]] = 'X'
                self.check_winner()
                self.server.update_game("player")
                self.robot_control.move(move[0] * 3 + move[1] + 1)
                return
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    possible_moves.append((i, j))
        if possible_moves:
            move = random.choice(possible_moves)
            self.board[move[0]][move[1]] = 'X'
            self.check_winner()
            self.server.update_game("player")
            self.robot_control.move(move[0] * 3 + move[1] + 1)
        else:
            self.check_winner()
            self.server.update_game("player")

    def find_possible_wins(self):
        possible_wins = []
        for j in range(3):
            if self.board[j][0] == self.board[j][1] != '_' and self.board[j][2] == '_':
                possible_wins.append((j, 2, self.board[j][0]))
            elif self.board[j][0] == self.board[j][2] != '_' and self.board[j][1] == '_':
                possible_wins.append((j, 1, self.board[j][0]))
            elif self.board[j][1] == self.board[j][2] != '_' and self.board[j][0] == '_':
                possible_wins.append((j, 0, self.board[j][1]))
        for i in range(3):
            if self.board[0][i] == self.board[1][i] != '_' and self.board[2][i] == '_':
                possible_wins.append((2, i, self.board[0][i]))
            elif self.board[0][i] == self.board[2][i] != '_' and self.board[1][i] == '_':
                possible_wins.append((1, i, self.board[0][i]))
            elif self.board[1][i] == self.board[2][i] != '_' and self.board[0][i] == '_':
                possible_wins.append((0, i, self.board[1][i]))
        if self.board[0][0] == self.board[1][1] != '_' and self.board[2][2] == '_':
            possible_wins.append((2, 2, self.board[0][0]))
        elif self.board[0][0] == self.board[2][2] != '_' and self.board[1][1] == '_':
            possible_wins.append((1, 1, self.board[0][0]))
        elif self.board[1][1] == self.board[2][2] != '_' and self.board[0][0] == '_':
            possible_wins.append((0, 0, self.board[1][1]))
        elif self.board[0][2] == self.board[1][1] != '_' and self.board[2][0] == '_':
            possible_wins.append((2, 0, self.board[0][2]))
        elif self.board[0][2] == self.board[2][0] != '_' and self.board[1][1] == '_':
            possible_wins.append((1, 1, self.board[0][2]))
        elif self.board[1][1] == self.board[2][0] != '_' and self.board[0][2] == '_':
            possible_wins.append((0, 2, self.board[1][1]))
        return possible_wins

    def check_winner(self):
        for j in range(3):
            if self.board[j][0] == self.board[j][1] == self.board[j][2] != '_':
                self.winner = self.board[j][0]
                return
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '_':
                self.winner = self.board[0][i]
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
            self.winner = self.board[0][2]
        elif all([self.board[i][j] != '_' for i in range(3) for j in range(3)]):
            self.winner = 'Draw'
        else:
            self.winner = None
        return
    
    def play(self):
        while not self.winner:
            print('Your turn')
            self.player_move_cognition()
            self.print_board()
            print('Computer`s turn')
            self.computer_move()
            self.print_board()
        if self.winner == 'O':
            print('You win')
        elif self.winner == 'X':
            print('You lose')
        else:
            print('Draw')


#
# if __name__ == '__main__':
#     game = GamePlay()
#     while True:
#         while True:
#             space = input('Enter space(1 ~ 9): ')
#             row = (int(space) - 1) // 3
#             col = (int(space) - 1) % 3
#             if game.player_move(row, col):
#                 break
#         for i in range(3):
#             print(*game.board[i])
#         print()
#         if game.winner is not None:
#             break
#         game.computer_move()
#         for i in range(3):
#             print(*game.board[i])
#         print()
#         if game.winner is not None:
#             break
#     if game.winner == 'Draw':
#         print('Draw')
#     elif game.winner == 'O':
#         print('You win')
#     else:
#         print('You lose')
