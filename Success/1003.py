import sys

n = int(sys.stdin.readline().strip())
nlist = [int(sys.stdin.readline().strip()) for _ in range(n)]

flist = [[1,0],[0,1]]

for i in nlist:
    for j in range(2,i+1):
        if j >= len(flist):
            flist.append([flist[j-1][0]+flist[j-2][0], flist[j-1][1]+flist[j-2][1]])        
    print(f"{flist[i][0]} {flist[i][1]}")


# 0 : 1 0
# 1 : 0 1
# 2 : 1 1
# 3 : 1 2
