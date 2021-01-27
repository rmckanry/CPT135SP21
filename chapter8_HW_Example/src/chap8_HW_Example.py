
found = False
y = [1, 2, 3, 4, 5, 6, 9, 11, 13]

for index in range(len(y)):
    if y[index] == 14:
        print("Found it")
        found = True
        break

if not found:
    print("not found")


