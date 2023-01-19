def rotate_number(n, k):
    k = k % len(str(n)) 
    if k > 0:
        return int(str(n)[-k:] + str(n)[:-k])
    else:
        return int(str(n)[k:] + str(n)[:k])

n = 12340056
k = 3
print(rotate_number(n, k))
