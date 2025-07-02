UserInput = int(input(">>"))
for i in range(1, UserInput + 1):
    print(' ' * (UserInput - i) + '*' * (2 * i - 1))