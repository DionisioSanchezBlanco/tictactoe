#Tic tac toe game easy way

xo_list = ["_"] * 9

def winner(pattern):
    if xo_list[0] + xo_list[1] + xo_list[2] == pattern \
        or xo_list[3] + xo_list[4] + xo_list[5] == pattern \
        or xo_list[6] + xo_list[7] + xo_list[8] == pattern \
        or xo_list[0] + xo_list[3] + xo_list[6] == pattern \
        or xo_list[1] + xo_list[4] + xo_list[7] == pattern \
        or xo_list[2] + xo_list[5] + xo_list[8] == pattern \
        or xo_list[0] + xo_list[4] + xo_list[8] == pattern \
        or xo_list[2] + xo_list[4] + xo_list[6] == pattern:
        return True

# To convert the coordinates to position in list
def converter(x,y):
    i = int(y) + 2
    j = int(x) - 1
    return (j * 3 + i) - 3

# Display the matrix
def display_matrix(xo_list):
    print("---------")
    for _i in range(0, 3):
        print(f"| {xo_list[_i * 3]} {xo_list[_i * 3 + 1]} {xo_list[_i * 3 + 2]} |")
    print("---------")

# To check if the cell contains a "X" or "O"
def check_position(xo_list, position):
    if xo_list[position] == "_":
        return False
    else:
        return True

# To check that coordinate values are a number
def check_format(x, y):
    try:
        x = int(x)
        y = int(y)
        return True
    except:
        return False

# To check range of the coordinates
def check_range(x, y):
    if 0 < int(x) < 4 and 0 < int(y) < 4:
        return True
    else:
        return False

display_matrix(xo_list)
x = None
y = None
turn = 1

while xo_list.count("_") > 0 or not(winner("XXX")) or not(winner("OOO")):
    x, y = input("Enter the coordinates: ").split()

    while check_format(x, y) == False:
        print("You should enter numbers!")
        x, y = input("Enter the coordinates: ").split()
        #check_format(x, y)

    while check_range(x, y) == False:
        print("Coordinates should be from 1 to 3!")
        x, y = input("Enter the coordinates: ").split()
        #check_range(x, y)

    position = converter(x, y)

    while check_position(xo_list, position) == True:
        print("This cell is occupied! Choose another one!")
        x, y = input("Enter the coordinates: ").split()
        position = converter(x, y)
        check_position(xo_list, position)

    if turn % 2 != 0:
        xo_list[position] = "X"
    else:
        xo_list[position] = "O"

    display_matrix(xo_list)
    turn += 1

    if winner("XXX"):
        print("X wins")
        break

    if winner("OOO"):
        print("O wins")
        break

    if turn == 10:
        print("Draw")
        break
