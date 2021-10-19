
import random
board = []

def initialize():
    initials = []
    while len(initials) != 20:
        possible = [random.randint(0,8), random.randint(0,8)]
        if possible not in initials:
            initials.append(possible)
    for i in range(9):
        line = []
        for i in range(9):
            line.append(' ')
        board.append(line)

    line_count = 0
    for line in board:
        item_count = 0
        for item in line:
            for row, column in initials:
                if row == line_count and column == item_count:
                    attempts = 0
                    while True:
                        possible = random.randint(1,9)
                        if check_row([row, column], possible) and check_empty([row, column]) and check_grid([row, column], possible) and check_column([row, column], possible):
                            board[line_count][item_count] = str(possible)
                            break
                        else:
                            attempts += 1
                            if attempts >= 20:
                                print("Maximum attempts reached... Try again later")
                                quit()
            item_count += 1
        line_count += 1
    display()

def display():
    line_count = 0
    for line in board:
        if line_count % 3 == 0 and line_count != 0:
            print("_______________________________________________")
        triplet1 = []
        triplet2 = []
        triplet3 = []
        count = 0
        for item in line:
            if count < 3:
                triplet1.append(item)
            elif count < 6:
                triplet2.append(item)
            else:
                triplet3.append(item)
            count += 1
        print(str(triplet1) + "|" + str(triplet2) + "|" + str(triplet3))
        line_count += 1
    found_space = False
    for line in board:
        for item in line:
            if item == ' ':
                found_space = True
    if found_space == False:
        print("You win!")
        quit()
    else:
        play()

def check_row(pos, number):
    row = pos[0]
    if  str(number) not in board[row]:
        return True
    else:
        return False

def check_empty(pos):
    row = pos[0]
    column = pos[1]
    if board[row][column] == ' ':
        return True
    else:
        return False

def check_column(pos, number):
    column = pos[1]
    for line in board:
        if str(number) in line[column]:
            return False
    return True

def check_grid(pos, number):
    numbers_grid = []
    row = pos[0]
    column = pos[1]
    if row < 3:
        grid_rows = [0, 1, 2]
    elif row < 6:
        grid_rows = [3, 4, 5]
    else:
        grid_rows = [6, 7, 8]
    if column < 3:
        grid_columns = [0, 1, 2]
    elif column < 6:
        grid_columns = [3, 4, 5]
    else:
        grid_columns = [6, 7, 8]
    for i in grid_rows:
        for j in grid_columns:
            numbers_grid.append(board[i][j])
    if str(number) not in numbers_grid:
        return True
    else:
        return False

def play():
    keep_playing = input("Do you want to keep playing? y/n")
    if keep_playing == 'n':
        quit()
    while True:
        user_row = int(input("Please input row. Remember that the first row is 0"))
        if user_row not in range(9):
            user_row = int(input("Please enter a valid row between 0-8"))
        else:
            break

    while True:
        user_column = int(input("Please input column. Rember that the first column is 0"))
        if user_column not in range(9):
            user_column = int(input("Please enter a valid column between 0-8"))
        else:
            break

    while True:
        user_number = int(input("Please input the number that you want"))
        if user_number not in range(1, 10):
            user_number = int(input("Please enter a valid number between 1-9"))
        else:
            break

    if check_row([user_row, user_column], user_number) and check_empty([user_row, user_column]) and check_grid([user_row, user_column], user_number) and check_column([user_row, user_column], user_number):
        board[user_row][user_column] = str(user_number)
    else:
        print("Invalid option. Please try again")
        play()
    display()


initialize()
