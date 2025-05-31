#Print an increasing number pattern from a users input

size = int(input("Enter the size of the pattern between 1 and 10: "))

while 1 <= size <= 10:
    for rows in range(1, size+1, 1):
        for columns in range(1, rows+1, 1):
            print(columns, end="")
        print("")
    size -= size
