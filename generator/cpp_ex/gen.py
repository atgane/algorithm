import random
rr = random.randint

MAX = rr(30000, 60000)
s = open("1.txt", "w")

N = rr(1, 9)
s.write(str(N) + '\n')