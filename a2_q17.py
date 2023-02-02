rows = int(input("Enter number of rows: ")) 
  
# It is used to print space  
k = 2 * rows - 2  
# Outer loop in reverse order  
for i in range(rows, -1, -1):  
    # Inner loop will print the number of space.  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    # This inner loop will print the number o stars  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()
