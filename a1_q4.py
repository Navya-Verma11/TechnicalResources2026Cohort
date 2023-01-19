def print_prime_numbers_till_n(n):
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
n=int(input("Enter an interger: "))
print(print_prime_numbers_till_n(n))
