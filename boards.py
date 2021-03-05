import random


def getboard(self, difficulty):
    if difficulty == "EASY":
        board_num = random.int(0, 3)
    if difficulty == "MEDIUM":
        board_num = random.int(3, 6)
    if difficulty == "HARD":
        board_num = random.int(6, 9)

    boards = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

    return boards[board_num]
