stars = int(input("enter the number of stars: "))
for i in range(stars):
    for i in range(i + 1):
        print('*', end=' ')
    print()
for i in range(stars, 0, -1):
    for i in range(i, 1, -1):
        print('*', end=' ')
    print()