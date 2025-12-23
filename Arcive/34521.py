import sys


n = int(sys.stdin.readline().strip())
nlist = [int(sys.stdin.readline().strip()) for _ in range(n)]

squares = {x*x for x in range(2, 1415)}

for i in nlist:
    if i == 1:
        print(1)
        continue
    
    curlist = [x for x in range(1, i + 1, 2)] + [x for x in range(2, i + 1, 2)]
    
    j = 0
    while j < i - 1:
        if (curlist[j] + curlist[j + 1]) in squares:
            if j + 2 < i:
                curlist[j + 1], curlist[j + 2] = curlist[j + 2], curlist[j + 1]
                j = max(0, j - 1)
            else:
                curlist[j + 1], curlist[0] = curlist[0], curlist[j + 1]
                j = 0
        else:
            j += 1
            
    print(*(curlist))

# for i in nlist:
#     curlist = [i for i in range(1,i+1)]
#     for j in range(i-1):
#         subsum = curlist[j] + curlist[j+1]
#         if subsum**0.5 == int(subsum**0.5):
#             tmp = curlist[j+2]
#             curlist[j+2] = curlist[j+1]
#             curlist[j+1] = tmp
#     print(" ".join(map(str, curlist)))