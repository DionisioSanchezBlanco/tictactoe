# Tic-tac-toe game

# Values to win
x_list = ["X", "X", "X"]
o_list = ["O", "O", "O"]

# Check rows to win
def check_rows(xo_list, x_list, o_list):
    first_row = [row for row in xo_list[0: 3]]
    second_row = [row for row in xo_list[3: 6]]
    third_row = [row for row in xo_list[6: 9]]
    winner_x = None
    winner_o = None
    draw = "draw"

    if first_row == x_list or second_row == x_list or third_row == x_list:
        winner_x = True
    
    if first_row == o_list or second_row == o_list or third_row == o_list:
        winner_o = True

    if winner_x == True and winner_o == True:
        return 3
    elif winner_x:
        return 1
    elif winner_o:
        return 2
    else:
        return draw


# Check columns to win
def check_columns(xo_list, x_list, o_list):
    first_column = [row for row in xo_list[0:9:3]]
    second_column = [row for row in xo_list[1:9:3]]
    third_column = [row for row in xo_list[2:9:3]]
    winner_x = None
    winner_o = None
    draw = "draw"

    if first_column == x_list or second_column == x_list or third_column == x_list:
        winner_x = True
    
    if first_column == o_list or second_column == o_list or third_column == o_list:
        winner_o = True

    if winner_x == True and winner_o == True:
        return 3
    elif winner_x:
        return 1
    elif winner_o:
        return 2
    else:
        return draw


# Check diagonal to win
def check_diagonal(xo_list, x_list, o_list):
    first_diagonal = [row for row in xo_list[0:9:4]]
    second_diagonal = [row for row in xo_list[2:8:2]]
    
    if first_diagonal == x_list or second_diagonal == x_list:
        return 1
    
    if first_diagonal == o_list or second_diagonal == o_list:
        return 2

# Check impossible game
# Difference betwen O and X is greater than 2        
def check_impossible(xo_list):
    x_counter = xo_list.count("X")
    o_counter = xo_list.count("O")

    # Get the absolute value
    if abs(x_counter - o_counter) >= 2:
        return True

def check_not_finished(xo_list):
    x_counter = xo_list.count("X")
    o_counter = xo_list.count("O")

    # Get the absolute value
    if abs(x_counter - o_counter) >= 2:
        return True

xo_string = input("Enter cells:").upper()
xo_list = [xo for xo in xo_string.strip()]

# Display the matrix
print("---------")
for _i in range(0, 3):
    print(f"| {xo_list[_i * 3]} {xo_list[_i * 3 + 1]} {xo_list[_i * 3 + 2]} |")
print("---------")


if check_impossible(xo_list):
    print("Impossible")
elif check_diagonal(xo_list, x_list, o_list) == 1:
    print("X wins")
elif check_diagonal(xo_list, x_list, o_list) == 2:
    print("O wins")
else:
    if check_rows(xo_list, x_list, o_list) == "draw" and check_columns(xo_list, x_list, o_list) == "draw":
        if xo_list.count("_") > 0:
            print("Game not finished")
        else:
            print("Draw")
    if check_rows(xo_list, x_list, o_list) == 3 or check_columns(xo_list, x_list, o_list) == 3:
        print("Impossible")
    if check_rows(xo_list, x_list, o_list) == 1 or check_columns(xo_list, x_list, o_list) == 1:
        print("X wins")
    if check_rows(xo_list, x_list, o_list) == 2 or check_columns(xo_list, x_list, o_list) == 2:
        print("O wins")
