n=int(input('Enter the number of rows:'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*',end='\t')
    for j in range(2*(n-i)):
        print(' ',end='\t')
    for j in range(i,0,-1):
        print('*',end='\t')
    print()  
for i in range(n):
    for j in range(i+1):
        print('*',end='\t')
    for j in range(2*(n-i-1)):
        print(' ',end='\t')
    for j in range(i+1):
        print('*',end='\t')
    print() 
