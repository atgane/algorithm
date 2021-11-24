import math

def is_prime_num(n):
    arr = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    arr[0] = False
    arr[1] = False
    return arr