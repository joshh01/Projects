#row = []
#column = []
#box = ()

board = [[1, 0, 0,  4, 5, 6,  7, 8, 9],
         [4, 0, 6,  7, 8, 9,  1, 2, 3],
         [7, 0, 9,  1, 2, 3,  4, 5, 6],

         [2, 0, 4,  0, 6, 7,  8, 9, 1],
         [5, 0, 7,  8, 0, 1,  2, 3, 0],
         [8, 0, 1,  0, 3, 4,  5, 6, 7],

         [3, 0, 5,  6, 7, 8,  9, 1, 2],
         [6, 0, 8,  0, 1, 2,  0, 4, 5],
         [9, 0, 2,  3, 4, 5,  6, 0, 8]]

boardCopy = []

"""
# for row in board:
#    for column in row:
#        print(column, end=" ")
#    print()

# Print / access rows
print(board[0])
# Print / access columns
print([row[0] for row in board])
# Print / access boxes
boxRow = ""
for x in range(3):
    for i in range(3):
        boxRow = boxRow + str(board[x][i]) + " "
    boxRow = boxRow + "\n"
print(boxRow)
"""


def getRow(y, array):
    return array[y - 1]


def getColumn(x, array):
    return [row[x - 1] for row in array]


def getBox(y, x, array):
    boxRow = [[], [], []]
    row = ""
    x = x - 1
    y = y - 1  # Lets us use from (1,1) --> (3,3) instead of (0,0) --> (2,2)
    x = 3 * x
    y = 3 * y
    for n in range(3):
        for z in range(3):
            row = row + str(array[x + n][z + y])
        boxRow[n] = row
        row = ""
    return boxRow


# print(getRow(1, board))
# print(getColumn(1, board))
# print(getBox(3, 2, board))


def getRowLengthNoZero(y, array):
    count = 0
    row = getRow(y, array)
    for value in row:
        if(value != 0):
            count = count + 1
    return count


def findOneMissingInRow(y, array):
    row = getRow(y, array)
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for value in row:
        for num in oneToNine:
            if(value == num):
                oneToNine.remove(num)
    if(len(oneToNine) == 1):
        return oneToNine[0], (row.index(0))


def getColumnLengthNoZero(x, array):
    count = 0
    column = getColumn(x, array)
    for value in column:
        if(value != 0):
            count = count + 1
    return count


def findOneMissingInColumn(x, array):
    column = getColumn(x, array)
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for value in column:
        for num in oneToNine:
            if(value == num):
                oneToNine.remove(num)
    if(len(oneToNine) == 1):
        return oneToNine[0], (column.index(0))


def getBoxSizeNoZero(x, y, array):
    count = 0
    box = getBox(x, y, array)
    for n in range(3):
        for s in range(3):
            if(int(box[n][s]) != 0):
                count = count + 1
    return count


def findOneMissingInBox(x, y, array):
    box = getBox(x, y, array)
    oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for z in range(3):
            for num in oneToNine:
                if(int(box[i][z]) == num):
                    oneToNine.remove(num)
    if(len(oneToNine) == 1):
        return oneToNine[0]


# print(getRowLengthNoZero(1))
# print(findOneMissingInRow(1))

# print("Row: 1")
# if(getRowLengthNoZero(1, board) == 8):
#     print("Missing Value: " + str(findOneMissingInRow(1, board)[0]))
#     print("Index: " + str(findOneMissingInRow(1, board)[1]))

# print(getColumnLengthNoZero(1))
# print(findOneMissingInColumn(1))

# print(getBoxSizeNoZero(1, 1))
# print(findOneMissingInBox(1, 1))
"""
rowCounter = 0
for row in board:
    rowCounter = rowCounter + 1
    if(getRowLengthNoZero(rowCounter) == 8):
        missingValue = findOneMissingInRow(rowCounter)[0]
        # MUST USE -1, as we use 1-9 instead of 0-8.
        missingValueIndex = findOneMissingInRow(rowCounter)[1]
        row[missingValueIndex] = missingValue

for row in board:
    for column in row:
        print(column, end=" ")
    print()
"""


def fillRows(array):
    rowCounter = 0
    for row in array:
        rowCounter = rowCounter + 1
        if(getRowLengthNoZero(rowCounter, array) == 8):
            missingValue = findOneMissingInRow(rowCounter, array)[0]
            # MUST USE -1, as we use 1-9 instead of 0-8.
            missingValueIndex = findOneMissingInRow(rowCounter, array)[1]
            row[missingValueIndex] = missingValue


def transpose(l1, l2):
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


def possible(num, x, y, array):
    #print(getRow(y, array))
    #print(getColumn(x, array))
    for i in getRow(y, array):
        if(i == num):
            return False
    for i in getColumn(x, array):
        if(i == num):
            return False
    if(x == 1 or x == 2 or x == 3):
        x = 1
    if(x == 4 or x == 5 or x == 6):
        x = 2
    if(x == 7 or x == 8 or x == 9):
        x = 3
    if(y == 1 or y == 2 or y == 3):
        y = 1
    if(y == 4 or y == 5 or y == 6):
        y = 2
    if(y == 7 or y == 8 or y == 9):
        y = 3
    box = getBox(x, y, array)
    for n in range(3):
        for s in range(3):
            if(int(box[n][s]) == num):
                return False
    return True


def checkAdjacentBoxes(x, y, array):
    box = getBox(x, y, array)
    leftBox = []
    leftLeftBox = []
    rightBox = []
    rightRightBox = []
    if(x == 2):
        leftBox = getBox(x - 1, y, array)
        rightBox = getBox(x + 1, y, array)

    print(box)
    print(leftBox)
    print(rightBox)


checkAdjacentBoxes(2, 3, board)
print(possible(5, 2, 2, board))

'''
for i in range(9):
    fillRows(board)
    transpose(board, boardCopy)
    board = []
    fillRows(boardCopy)
    transpose(boardCopy, board)
    boardCopy = []
'''

for row in board:
    for column in row:
        print(column, end=" ")
    print()
