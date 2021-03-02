# Evan McKague 
# Sudoku in Python


class Sudoku:

    def __init__(self):
        self._game_board = [["____"] * 9 for i in range(9)]
        self._game_state = "UNFINISHED"
        self._difficulty = self.get_difficulty()
        self._set_board = self.set_board()
        self._print_board = self.print_board()

    def get_difficulty(self):
        """TO DO
        """
        pass
    def set_board(self):
        """TO DO
        """
        pass
    def print_board(self):
        """TO DO
        """
        rowNum = 9
        alpha = ["  a", "  b", "  c", "  d", "  e", "  f", "  g", "  h", "  i"]
        for row in self._game_board:
            temp = []
            for el in row:
                temp.append(el)

            print(rowNum, "  ", '|'.join(temp[0:]))
            rowNum -= 1
        print("    ", '  '.join(alpha[0:]))
        print('\n')

game = Sudoku()
