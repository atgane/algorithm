import os
import sys

case_num = 1
while True:
    os.system('python3 gen.py')
    os.system('python3 test1.py')
    os.system('python3 test2.py')
    s1 = open('out1.txt', 'r')
    s2 = open('out2.txt', 'r')

    c1 = s1.read()
    c2 = s2.read()

    length = max(len(c1), len(c2))
    for i in range(length):
        if c1[i] != c2[i]:
            print('find!')
            s = open('1.txt', 'r')
            case = s.read()
            print('case:')
            print(case)
            s1.close()
            s2.close()
            s.close()
            sys.exit()

    print('exploring wrong case... case num:', case_num)
    case_num += 1