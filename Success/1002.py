import sys

xylist = []

t = int(sys.stdin.readline().strip())

for _ in range(t):
    xyr = list(map(int,sys.stdin.readline().strip().split()))
    xylist.append(xyr)
    
for i in range(0, t):
    x1 = xylist[i][0]
    y1 = xylist[i][1]
    r1 = xylist[i][2]
    x2 = xylist[i][3]
    y2 = xylist[i][4]
    r2 = xylist[i][5]
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if dist == 0 and r1 == r2: # 두 원이 같은 원
        print(-1)
    elif dist > r1 + r2: # 두 원이 떨어져 있음
        print(0)
    elif dist < abs(r1 - r2): # 내부에 있는 원이 접하지 않음
        print(0)
    elif dist == r1 + r2: # 외접
        print(1)
    elif dist == abs(r1 - r2): # 내접
        print(1)
    elif abs(r1 - r2) < dist < r1 + r2: # 두 원이 두 점에서 만남
        print(2)
    else:
        print("error")