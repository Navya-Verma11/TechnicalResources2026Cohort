num = input("Enter a number: ")
count = 0
for i in num:
    if i.isdigit():
        count += 1
print("Number of digits: ", count)
