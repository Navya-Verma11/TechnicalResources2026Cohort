def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if(
                    # first column
                    (column == 0) or

                    # last column
                    (column == n-1) or

                    # left slanting line
                    (row+column == n-1 and row >= n//2) or

                    # right slanting line
                    (row == column and row >= n//2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))
print_pattern(size)
