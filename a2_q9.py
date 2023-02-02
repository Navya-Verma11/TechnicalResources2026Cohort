# Hollow Diamond pattern

# Reading number of row
row = int(input('Enter number of row: '))

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print("\t", end="")
    for j in range(1, 2*i+1):
        if j==1 or j==2*i:
            print("*", end="")
        else:
            print("\t", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print("\t", end="")
    for j in range(1, 2*i+1):
        if j==1 or j==2*i:
            print("*", end="")
        else:
            print("\t", end="")
    print()
