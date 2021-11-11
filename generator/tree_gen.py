import random
import math
import string
rr = random.randint


s = open("1.txt", "w")

N = rr(40, 40)
s.write(str(N) + "\n")

check_list = [0 for _ in range(N + 1)]

s.write("1 2 2 \n")
check_list[1] = 1
check_list[2] = 1
for _ in range(N - 2):
    t1, t2 = rr(1, N), rr(1, N)
    while (check_list[t1] == check_list[t2]):
        t1, t2 = rr(1, N), rr(1, N)
    s.write(str(t1) + " " + str(t2) + " " + str(rr(1, 6)) + '\n')
    check_list[t1] = 1
    check_list[t2] = 1

Q = rr(3, 10)
s.write(str(Q) + "\n")
for _ in range(Q):
    t = rr(1, 2)
    if t == 1:
        s.write(str(t) + " " + str(rr(1, N)) + " " + str(rr(1, N)) + "\n")
    else:
        s.write(str(t) + " " + str(rr(1, N)) + " " + str(rr(1, N)) + " " + str(rr(1, int(math.log2(N)))) + "\n")