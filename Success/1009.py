import sys

n = int(sys.stdin.readline().strip())

ablist = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in ablist:
    a, b = i
    res = 1
    a = a % 10
    while b > 0:
        if b % 2 == 1:
            res = res * a % 10
        a = a * a % 10
        b = b // 2
    print(res if res != 0 else 10)