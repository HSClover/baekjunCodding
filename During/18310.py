import sys

N = int(sys.stdin.readline().strip())
houses = list(map(int,sys.stdin.readline().split()))

# min_distance = int(1e9)
# min_house = houses[0]
    
# for i in houses:
#     distance = 0
#     for j in houses:
#             distance += abs(i - j)
#     min_distance = min(min_distance, distance)
#     min_house = i if min_distance == distance else min_house

# print(min_house)

houses.sort()
if N % 2 == 1:
    print(houses[N // 2])
else:
    print(houses[(N-1) // 2])