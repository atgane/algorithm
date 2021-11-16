import sys
sys.stdin = open('1.txt', 'r')
sys.stdout = open('out1.txt', 'w')
ssr = sys.stdin.readline

ssr()[:-1]
print(1)