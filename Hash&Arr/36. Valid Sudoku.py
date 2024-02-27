# 36. Valid Sudoku
from collections import defaultdict


def solution(board):
    row, col, box = {}, {}, {}
    for r in range(len(board)):
        for c in range(len(board)):
            current = board[r][c]

            # Row check
            if r not in row:
                row[r] = [current]
            else:
                if current != '.' and current in row[r]:
                    return False
                row[r].append(current)

            # Col check
            if c not in col:
                col[c] = [current]
            else:
                if current != '.' and current in col[c]:
                    return False
                col[c].append(current)

            # Box check
            if r < 3:
                if c < 3:
                    i = 0
                elif c < 6:
                    i = 1
                elif c < 9:
                    i = 2
            elif r < 6:
                if c < 3:
                    i = 3
                elif c < 6:
                    i = 4
                elif c < 9:
                    i = 5
            elif r < 9:
                if c < 3:
                    i = 6
                elif c < 6:
                    i = 7
                elif c < 9:
                    i = 8

            if i not in box:
                box[i] = [current]
            else:
                if current != '.' and current in box[i]:
                    return False
                box[i].append(current)

    return True


a = [["5", "1", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", '3']
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

b = [["8", "1", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(solution(a))

hMap = {1:['1','2','.']}
#for i in range(3):
#    if '2' in hMap[1]:
#        print('true')