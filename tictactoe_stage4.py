#Tic tac toe game easy way

s = input("Enter cells: ").upper()

xo_list = [xo for xo in s.strip()]
srep = s.replace("_", " ")

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
def display_matrix(srep):
    print("---------")
    for _i in range(0, 3):
        print(f"| {srep[_i * 3]} {srep[_i * 3 + 1]} {srep[_i * 3 + 2]} |")
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

display_matrix(srep)
x = None
y = None

if xo_list.count("_") > 0:
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

    xo_list[position] = "X"
    display_matrix(xo_list)


else:
    if abs(xo_list.count("X") - xo_list.count("O")) >= 2:
        print("Impossible")
    elif winner("XXX") == True and winner("OOO") == True:
        print("Impossible")
    elif winner("XXX") == True:
        print("X wins")
    elif winner("OOO") == True:
        print("O wins")
    elif xo_list.count("_") > 0:
        print("Game not finished")
    else:
        print("Draw")
