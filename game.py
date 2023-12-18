import random


class GamePlay:
    def __init__(self):
        self.board = [['_' for i in range(3)] for j in range(3)]
        self.winner = None

    def player_move(self, row, col):
        if row not in range(3) or col not in range(3):
            print('Invalid Move')
            return False
        if self.board[row][col] != '_':
            print('Invalid Move')
            return False
        self.board[row][col] = 'O'
        self.check_winner()
        return True

    def computer_move(self):
        move = self.find_possible_win()
        if move:
            if random.randint(0, 1) == 0:
                self.board[move[0]][move[1]] = 'X'
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    possible_moves.append((i, j))
        if possible_moves:
            move = random.choice(possible_moves)
            self.board[move[0]][move[1]] = 'X'
        self.check_winner()

    def find_possible_win(self):
        for j in range(3):
            if self.board[j][0] == self.board[j][1] != '_' and self.board[j][2] == '_':
                return j, 2
            elif self.board[j][0] == self.board[j][2] != '_' and self.board[j][1] == '_':
                return j, 1
            elif self.board[j][1] == self.board[j][2] != '_' and self.board[j][0] == '_':
                return j, 0
        for i in range(3):
            if self.board[0][i] == self.board[1][i] != '_' and self.board[2][i] == '_':
                return 2, i
            elif self.board[0][i] == self.board[2][i] != '_' and self.board[1][i] == '_':
                return 1, i
            elif self.board[1][i] == self.board[2][i] != '_' and self.board[0][i] == '_':
                return 0, i
        if self.board[0][0] == self.board[1][1] != '_' and self.board[2][2] == '_':
            return 2, 2
        elif self.board[0][0] == self.board[2][2] != '_' and self.board[1][1] == '_':
            return 1, 1
        elif self.board[1][1] == self.board[2][2] != '_' and self.board[0][0] == '_':
            return 0, 0
        elif self.board[0][2] == self.board[1][1] != '_' and self.board[2][0] == '_':
            return 2, 0
        elif self.board[0][2] == self.board[2][0] != '_' and self.board[1][1] == '_':
            return 1, 1
        elif self.board[1][1] == self.board[2][0] != '_' and self.board[0][2] == '_':
            return 0, 2
        else:
            return None

    def check_winner(self):
        for j in range(3):
            if self.board[j][0] == self.board[j][1] == self.board[j][2] != '_':
                self.winner = self.board[j][0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '_':
                self.winner = self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
            self.winner = self.board[0][2]
        elif all([self.board[i][j] != '_' for i in range(3) for j in range(3)]):
            self.winner = 'Draw'
        else:
            self.winner = None


if __name__ == '__main__':
    game = GamePlay()
    while game.winner is None:
        while True:
            space = input('Enter space(1 ~ 9): ')
            row = (int(space) - 1) // 3
            col = (int(space) - 1) % 3
            if game.player_move(row, col):
                break
        for i in range(3):
            print(*game.board[i])
        print()
        game.computer_move()
        for i in range(3):
            print(*game.board[i])
        print()
    match game.winner:
        case 'O':
            print('You Win')
        case 'X':
            print('You Lose')
        case 'Draw':
            print('Draw')