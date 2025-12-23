import sys

N = int(sys.stdin.readline().strip())
houses = list(map(int,sys.stdin.readline().split()))

houses.sort()
if N % 2 == 1:
    print(houses[N // 2])
else:
    print(houses[(N-1) // 2])