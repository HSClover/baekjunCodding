import sys

n = int(sys.stdin.readline().strip())
checkNum = 1
pos = 1
finish = False

while finish == False:
    if checkNum % n == 0:
        finish == True
    else:
        checkNum += 10**pos
        pos += 1
        
print(pos)