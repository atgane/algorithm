import random
rr = random.randint


s = open("1.txt", "w")

N = rr(1000, 1500)
s.write(str(N) + "\n")
for _ in range(N):
    s.write(str(rr(1, 9)) + " ")
s.write("\n")

a, b = rr(1, N), rr(1, N)
if a > b:
    a, b = b, a
s.write(str(a) + " " + str(b))