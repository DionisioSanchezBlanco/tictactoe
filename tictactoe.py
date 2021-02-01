# Tic-tac-toe game
xo_string = input("Enter cells:")
xo_list = list(xo_string)

print("---------")
for _i in range(0, 3):
    print(f"| {xo_list[_i * 3]} {xo_list[_i * 3 + 1]} {xo_list[_i * 3 + 2]}|")
print("---------")