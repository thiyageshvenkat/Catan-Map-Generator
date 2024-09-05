import random
tiles = list("🌊" * 21 + "🌾" * 7 + "🗻" * 7 + "🧱" * 7 + "🐑" *7 + "🌳" * 7 + "🌵" * 3 +  "🪙" * 4)
random.shuffle(tiles)
board = []
for i in range(10):
    board.append([])
    for j in range(10):
        board[i].append(' ')
for i in range(8):
    board[0][1 + i] = tiles.pop(0)
for i in range(9):
    board[1][1 + i] = tiles.pop(0)
for i in range(10):
    board[2][i] = tiles.pop(0)
for i in range(9): ##### THE MIDDLE ONE WITH THE BUILT IN OCEAN TILES
    board[3][1 + i] = tiles.pop(0)
for i in range(10):
    board[4][i] = tiles.pop(0)
for i in range(9):
    board[5][1 + i] = tiles.pop(0)
for i in range(8):
    board[6][1 + i] = tiles.pop(0)
print("\nThe top-most row of the map displayed represents the longer edge of the Seafarers map. \nThe middle row of the map displayed contains only 9 tiles, because the first and last two tiles of the eight tiles of that row must be ocean.")
print("Catan Seafarers 5-6 Player Board: \n")
for i in range(len(board)):
    if i % 2 == 1:
        print(" ", *board[i])
    else:
        print("  ", *board[i])
numbers = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12]
numbers = [str(i) for i in numbers] 
random.shuffle(numbers)
board_numbers = board
for i in range(len(board_numbers)):
    for j in range(len(board_numbers[i])):
        if board_numbers[i][j] != "🌊" and board_numbers[i][j] != " " and board_numbers[i][j] != "🌵":
            board_numbers[i][j] = numbers.pop(0)
        elif board_numbers[i][j] == "🌊":
            board_numbers[i][j] = "~"
print("\n")
print("Numbers:")
for i in range(len(board_numbers)):
    if i % 2 == 1:
        print(" ")
        for j in board_numbers[i]:
            print(j.ljust(3), end = "")
    else:
        print("  ")
        for j in board_numbers[i]:
            print(j.ljust(3), end = "")
