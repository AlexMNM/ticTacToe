import numpy as np
import inquirer

SYMBOLS = ('X', 'O')

class Score:
    def __init__(self) -> None:
        self.values = {'rows':[0, 0, 0], 'cols':[0, 0, 0], 'diags':[0, 0]}

    def inc(self, field, index) -> None:
        self.values[field][index] += 1

class Board():
    def __init__(self) -> None:
        self.matrix = np.full((3, 3), dtype=str, fill_value=" ")
        self.scores = {SYMBOLS[0]:Score(), SYMBOLS[1]:Score()}
    
    def putSymbol(self, symbol, row, col) -> None:
        self.matrix[row, col] = symbol
        self.scores[symbol].inc('rows', row)
        self.scores[symbol].inc('cols', col)
        if [row, col] in [[1, 1]]:
            self.scores[symbol].inc('diag', 0)
            self.scores[symbol].inc('diag', 1)
        elif [row, col] in [[0, 0], [2, 2]]:
            self.scores[symbol].inc('diag', 0)
        elif [row, col] in [[0, 2], [2, 0]]:
            self.scores[symbol].inc('diag', 1)
    
    def getScore(self, symbol) -> Score:
        return self.scores[symbol]


class Player():
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.myScore = Score()

    def putMySymbol(self, board:Board, row, col) -> None:
        board.putSymbol(self.symbol, row, col)

    def getMyScore(self, board:Board) -> Score:
        return board.getScore(self.symbol)

# Prepare user dialogue
questions = [
    inquirer.List(
        "symbol",
        message="What do you want to play as?",
        choices=SYMBOLS
    )
]


def turn(nr, board, player:Player, other_player:Player):
    # Start with first line
    danger = 'rows'
    # Check score of other player
    op_score = other_player.getMyScore(board)
    for field in op_score:
        if op_score[field] == 2:
            danger = field




def main() -> None:
    # Init
    board = Board()

    # Ask player X or O
    answer = inquirer.prompt(questions)
    player_choice = SYMBOLS.index(answer["symbol"])

    turn_number = 0


    


if __name__ == '__main__':
    main()
