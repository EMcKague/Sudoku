# Evan McKague
# Sudoku in Python
import time
import pygame
from boards import getboard
from sudoku_solver import finish, valid_sol, find_empty_square
pygame.init()


class Board:

    def __init__(self, difficulty="MEDIUM"):
        self._board = self.create_board(difficulty)
        self._rows = 9
        self._cols = 9
        self._width = 540
        self._height = 540
        self._margin = self._width / 9
        self._squares = [[Square(self._board[i][ii], i, ii, self._width,
                         self._height) for ii in range(self._cols)]
                         for i in range(self._rows)]
        self._selected = None
        self._duplicate = self.generate_duplicate_board()
        self._set_up_board = self.set_up_board()
        self._colors = {
            "BLACK": (0, 0, 0),
            "GRAY": (191, 191, 191),
            "GREEN": (0, 212, 14),
            "WHITE": (250, 250, 250),
            "RED": (255, 94, 94)
        }

    def create_board(self, difficulty):
        """FUTURE TO DO, Gets a auto generated board from sudoku_board
        idea:
        board =[sudoku_board.boards.get_board("MEDIUM") * 9 for i in range(10)]
        """

        board = getboard()

        return board

    def generate_duplicate_board(self):
        """Finds all the values in squares and then creates a model
        based on values. Used to solve and check solutions
        """
        duplicate = [[self._squares[i][ii]._value for ii in
                     range(self._cols)] for i in range(self._rows)]

        return duplicate

    def place_val(self, val):
        """
        """
        # get the selected square
        row, col = self._selected

        self._squares[row][col].set_val(val)
        self._duplicate = self.generate_duplicate_board()

    def draw_board(self, surf):
        """
        """
        black = self._colors["BLACK"]

        # Grid lines
        for i in range(self._rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1

            margin = i * self._margin
            pygame.draw.line(surf, (black), (0, margin),
                             (self._width, margin), thick)
            pygame.draw.line(surf, (black), (margin, 0),
                             (margin, self._height), thick)

        # Squares
        # print(self._squares)
        for i in range(self._rows):
            for ii in range(self._cols):
                # print("i=", i, 'ii=', ii)
                self._squares[i][ii].draw_square(surf)

    def click_location(self, pos):
        """
        """
        print('pos[0]=', pos[0], 'pos[1]=', pos[1])

        if pos[0] < self._width and pos[1] < self._height:
            col = pos[0] // self._margin
            row = pos[1] // self._margin

            return {"SQUARE": (int(row), int(col))}

        if (pos[0] > 370 and pos[0] < 428) and (pos[1] > 556 and pos[1] < 596):
            return {"FINISH": 0}

        if (pos[0] > 448 and pos[0] < 509) and (pos[1] > 556 and pos[1] < 596):
            return {"SOLVE": 0}
        else:
            return None

    def set_selected(self, row, col):
        """
        """
        # iterates through each space and sets them all to false
        for i in range(self._rows):
            for ii in range(self._cols):
                self._squares[i][ii]._selected = False

        # finds the correct space, and sets it to true
        # updates selected in board
        self._squares[row][col]._selected = True
        self._selected = (row, col)

    def set_up_board(self):
        # iterate through each space in squares
        for i in range(self._rows):
            for ii in range(self._cols):
                if self._squares[i][ii]._value != 0:
                    self._squares[i][ii]._immutable = True
                    self._squares[i][ii]._color = (191, 191, 191)

    def clear_square(self):
        """
        """
        row, col = self._selected
        # if square isn't immutable
        if not self._squares[row][col]._immutable:
            # set val to 0
            self._squares[row][col].set_val(0)

    def mics_boxes(self, surf, play_time, end=False):
        """
        """
        black = (0, 0, 0)
        green = (0, 212, 14)
        white = (245, 245, 245)
        x_loc = self._rows + self._height - 300
        y_loc = self._height + 15
        largefont = pygame.font.SysFont("arial", 20, 1)

        # timer
        pygame.draw.rect(surf, green, (x_loc - 50, y_loc, 150, 40))
        pygame.draw.rect(surf, black, (x_loc - 50, y_loc, 150, 40), 3)
        text = largefont.render(self.get_timer(play_time), 1, black)
        surf.blit(text, (x_loc, y_loc + 5))

        # score
        text = largefont.render("SCORE:", 1, black)
        surf.blit(text, (10, y_loc + 10))
        pygame.draw.rect(surf, black, (x_loc - 150, y_loc, 85, 40), 3)
        if end:
            text = largefont.render("0", 1, black)
        else:
            text = largefont.render(self.get_score(play_time), 1, black)
        surf.blit(text, (x_loc - 135, y_loc + 5))

        # Finish button
        x_loc = self._rows + self._height - 180
        smallfont = pygame.font.SysFont("Corbel", 20, 1)
        text = smallfont.render("Finish", True, white)
        pygame.draw.rect(surf, black, (x_loc, y_loc, 60, 40))
        surf.blit(text, (x_loc + 9, y_loc + 12))

        # Solve button
        x_loc = self._rows + self._height - 100
        smallfont = pygame.font.SysFont("Corbel", 20, 1)
        text = smallfont.render("Solve", True, black)
        pygame.draw.rect(surf, black, (x_loc, y_loc, 60, 40), 3)
        surf.blit(text, (x_loc + 9, y_loc + 12))

        # Rules
        y_loc = y_loc + 50
        x_loc = 10
        pygame.draw.rect(surf, black, (x_loc, y_loc, 500, 90), 3)
        text = pygame.font.SysFont("arial", 15, 1)
        rules1 = text.render("** Normal Sudoku rules apply", 1, black)
        rules2 = text.render('* Left click on a cell and press a '
                             'key 1-9 to input a number', 1, black)
        rules3 = text.render(
                             '* Press '
                             'delete or backspace to remove a number',
                             1, black)
        rules4 = text.render('* Press finish button to see if answer '
                             'is correct',
                             1, black)
        rules5 = text.render('* Press solve for the board to be'
                             ' filled in with solution (score = 0)', 1, black)

        surf.blit(rules1, (15, y_loc + 10))
        surf.blit(rules2, (15, y_loc + 25))
        surf.blit(rules3, (15, y_loc + 40))
        surf.blit(rules4, (15, y_loc + 55))
        surf.blit(rules5, (15, y_loc + 70))

    def get_timer(self, secs):
        sec = secs % 60
        minute = secs // 60
        new_time = str(minute) + ":" + str(sec).zfill(2)
        return new_time

    def get_score(self, secs):
        diff = (secs // 5) * 2
        score = 1000 - diff
        if score < 0:
            score = 0
        return str(score)

    def print_failure_msg(self, surf):
        red = (255, 94, 94)
        x_loc = self._width/2 - 50
        y_loc = self._width/2 - 50
        print("creating failure msg")
        largefont = pygame.font.SysFont("arial", 40, 1)
        text = largefont.render("INCORRECT!", 1, red)
        surf.blit(text, (x_loc, y_loc))
        pygame.display.update()
        time.sleep(3)

    def print_success_msg(self, surf):
        red = (255, 94, 94)
        x_loc = self._width/2 - 50
        y_loc = self._width/2 - 50
        print("creating success msg")
        largefont = pygame.font.SysFont("arial", 40, 1)
        text = largefont.render("YOU WIN!", 1, red)
        surf.blit(text, (x_loc, y_loc))
        pygame.display.update()
        time.sleep(3)

    def solve(self, surf, play_time, board):
        empty_square = find_empty_square(self._duplicate)
        if not empty_square:
            print("returning True")
            return True

        row, col = empty_square
        for i in range(1, 10):
            if valid_sol(self._duplicate, i, (row, col)):
                self._duplicate[row][col] = i
                self._squares[row][col].set_val(i)

                redraw_surface(surf, board, play_time)
                pygame.display.update()
                pygame.time.delay(30)

                if self.solve(surf, play_time, board):
                    return True

                self._duplicate[row][col] = 0
                self._squares[row][col].set_val(0)
                redraw_surface(surf, board, play_time)
                pygame.display.update()
                pygame.time.delay(30)
        # print("returning False")
        return False


class Square:

    def __init__(self, value, row, col, width, height):
        self._value = value
        self._row = row
        self._col = col
        self._width = width
        self._height = height
        self._margin = self._width / 9
        self._immutable = False
        self._selected = False
        self._color = None

    def set_val(self, val):
        self._value = val

    def draw_square(self, surf):
        """
        """
        # Create vars to help with drawing
        font = pygame.font.SysFont('arial', 40)
        x = self._col * self._margin
        y = self._row * self._margin

        # if immutable fill draw grey rect
        if self._color:
            surf.fill(self._color, rect=[x + 2.5, y + 2.5,
                      self._margin - 3, self._margin - 3])

        # render text value if it's not 0
        if self._value != 0:
            text = (font.render(str(self._value), 1, (0, 0, 0)))
            destination = (x + (self._margin/2 - text.get_width()/2),
                           y + (self._margin/2 - text.get_height()/2))
            surf.blit(text, (destination[0], destination[1]))

        # blit (what you are displaying, (destination of display))

        # highlight selected piece
        if self._selected:
            # draw rect params,
            # (the surface you want it on, the color you want it,
            # (x axis location, y axis location, width of rect, height of rect)
            # , Thickness of border)
            pygame.draw.rect(surf, (255, 0, 0),
                             (x + 1, y + 1,
                             self._margin - 2, self._margin - 1.5),
                             4)


def redraw_surface(surf, board, play_time, end=False):
    white = (255, 255, 255)
    surf.fill((white))
    # print("play_time in redraw", play_time)
    if end:
        board.mics_boxes(surf, play_time, end)
    else:
        board.mics_boxes(surf, play_time)

    # font = pygame.font.SysFont('arial', 40)
    board.draw_board(surf)


def main():
    # create surface, size 540, 600
    surf = pygame.display.set_mode((540, 700))
    # Change title for surface
    pygame.display.set_caption("SUDOKU")
    # Instantiate board
    board = Board()
    start = time.time()
    stop = 0
    end = False
    solved = False
    running = True
    key = None

    while running:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            # standard exit pygame
            if event.type == pygame.QUIT:
                running = False

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
                print("event.key =", event.key, pygame.K_DELETE)
                # set up delete key
                if (event.key == pygame.K_DELETE
                   or event.key == pygame.K_BACKSPACE):
                    print("deleting")
                    board.clear_square()
                    key = None

                # set up enter key
                # if event.key == pygame.K_RETURN:
                #     board.place

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos[0], pos[1])

                clicked = board.click_location(pos)
                if clicked:

                    if "FINISH" in clicked:
                        print("calling finished function")
                        # pause time
                        # pause_game = time.time()
                        # redraw_surface(surf, board, pause_game)
                        # call finish function
                        print(board._duplicate)
                        done = finish(board._duplicate)
                        print("is done?", done)
                        if done:
                            # print validation msg
                            board.print_success_msg(surf)
                            # stop time
                            end = True
                        else:
                            # print try again msg
                            print("NOT DONE")
                            board.print_failure_msg(surf)
                            redraw_surface(surf, board, play_time)

                    if "SQUARE" in clicked:
                        row, col = clicked["SQUARE"]
                        board.set_selected(row, col)
                        key = None

                    if "SOLVE" in clicked:
                        print("calling solve function")
                        # set score to 0
                        solved = True
                        # stop time
                        stop = play_time
                        # call solve function
                        board.solve(surf, play_time, board)

        if board._selected and key:
            if not board._squares[row][col]._immutable:
                board.place_val(key)

        if solved:
            redraw_surface(surf, board, stop, True)
            pygame.display.update()
        elif end and not solved:
            redraw_surface(surf, board, stop)
            pygame.display.update()
        else:
            redraw_surface(surf, board, play_time)
            pygame.display.update()


main()
pygame.quit()
