#Tic tac toe game easy way

s = input("Enter cells: ").upper()

xo_list = [xo for xo in s.strip()]
print(xo_list)

def winner(pattern):
    if s[0] + s[1] + s[2] == pattern \
        or s[3] + s[4] + s[5] == pattern \
        or s[6] + s[7] + s[8] == pattern \
        or s[0] + s[3] + s[6] == pattern \
        or s[1] + s[4] + s[7] == pattern \
        or s[2] + s[5] + s[8] == pattern \
        or s[0] + s[4] + s[8] == pattern \
        or s[2] + s[4] + s[6] == pattern:
        return True

# Display the matrix
print("---------")
for _i in range(0, 3):
    print(f"| {xo_list[_i * 3]} {xo_list[_i * 3 + 1]} {xo_list[_i * 3 + 2]} |")
print("---------")

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
