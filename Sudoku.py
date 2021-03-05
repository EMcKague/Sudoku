# Evan McKague
# Sudoku in Python

import pygame
import sudoku_boards
pygame.init()


class Board:

    def __init__(self, difficulty="MEDIUM"):
        self._board = self.create_board(difficulty)
        self._rows = 9
        self._cols = 9
        self._width = 540
        self._hieght = 540
        self._squares = [[Square(self._board[i][ii], i, ii, width, height)
                         for ii in range(cols) for i in range(rows)]]
        self._selected = None
        self._duplicate = None

    def create_board(self, difficulty):
        """FUTURE TO DO, Gets a auto generated board from sudoku_board
        idea:
        board =[sudoku_board.boards.get_board("MEDIUM") * 9 for i in range(10)]
        """

        board = [
                    [3, 0, 6, 5, 0, 8, 4, 0, 0],
                    [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5],
                    [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]
                ]

        return board

    def generate_duplicate_board(self):
        """Finds all the values in squares and then creates a model
        based on values. Used to solve and check solutions
        """
        self._duplicate = [[self._squares[i][ii].value for ii in
                           range(self.cols)] for i in range(self._rows)]

    def place_val(self, val):
        """
        """
        # get the selected square
        row, col = self._selected

        self._squares[row][col].set_val(val)
        self.update_model()


class Square:

    def __init__(self, value, row, col, width, height):
        self._value = value
        self._row = row
        self._col = col
        self._width = width
        self._height = height
        self._selected = False

    def set_val(self, val):
        self._value = val

    def draw_square(self, surf):
        """
        """
        # Create vars to help with drawing
        font = pygame.font.SysFont('arial', 40)
        margin = self._width / 9
        x_axis = self._col * margin
        y_axis = self._row * margin
        text = (fnt.render(str(self._value), 1, (0, 0, 0)))
        destination = (x + (margin/2 - text.get_width()/2),
                      y + (margin/2 = text.get_height()/2)

        # drawing the square
        # blit (what you are displaying, (destination of display))
        surf.blit(text, (destination[0],destination[1]))

        if self._selected:
            # highlight selected piece
            pygame.draw.rect(surf, (255, 0, 0), (x, y, margin, margin), 3)

def get_time():
    """Function to get time
    """

def get_score():
    """Function to get score
    """
def main():
    surf = pygame.display.set_mode(600, 600)
    board = BackedArray()

    run = True
    key = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                # set up keys 1 - 9
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                # set up delete key
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                # set up enter key
                if event.key == pygame.K_RETURN:
                    board.place

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = True

                # Grid
                if pos[0] < width and pos[1] < height:
                    recreate(board,)
