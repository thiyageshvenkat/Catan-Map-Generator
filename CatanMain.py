import random
tiles = list("🌾" * 4 + "🗻" * 3 + "🧱" * 3 + "🐑" * 4 + "🌳" * 4 + "🌵")
random.shuffle(tiles)
board = []
for i in range(6):
    board.append([])
    for j in range(6):
        board[i].append(' ')
for i in range(3):
    board[0][1 + i] = tiles.pop(0)
for i in range(4):
    board[1][1 + i] = tiles.pop(0)
for i in range(5):
    board[2][i] = tiles.pop(0)
for i in range(4): 
    board[3][1 + i] = tiles.pop(0)
for i in range(3):
    board[4][1 + i] = tiles.pop(0)
print("Catan Main Game Board: \n")
for i in range(len(board)):
    if i % 2 == 1:
        print(" ", *board[i])
    else:
        print("  ", *board[i])
numbers = [3, 4, 5, 6, 8, 9, 10, 11, 3, 4, 5, 6, 8, 9, 10, 11, 2, 12]
numbers = [str(i) for i in numbers] 
random.shuffle(numbers)
board_numbers = board
for i in range(len(board_numbers)):
    for j in range(len(board_numbers[i])):
        if board_numbers[i][j] != " " and board_numbers[i][j] != "🌵":
            board_numbers[i][j] = numbers.pop(0)
            
print("\n")
print("Numbers:")
for i in range(len(board_numbers)):
    if i % 2 == 1:
        print(" ")
        for j in board_numbers[i]:
            print(j.rjust(3).ljust(4), end = "")
    else:
        print("  ")
        for j in board_numbers[i]:
            print(j.rjust(3).ljust(4), end = "")

harbors = ["3:1", "3:1", "3:1", "3:1", "2:1 Pasture", "2:1 Wood", "2:1 Wool", "2:1 Clay", "2:1 Ore", "2:1 Grain"]
random.shuffle(harbors)
print("\n\nHarbors starting from the 2:1 Clay Harbor:")
for i in harbors:
    print("⚓", i, end = "  ")
