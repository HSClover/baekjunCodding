import sys

def solve():
    try:
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
    except:
        return

    if N < 3:
        return

    A.sort()
    min_abs = float('inf')
    result = [] 

    for i in range(N - 2):
        L = i + 1
        R = N - 1

        while L < R:
            current_sum = A[i] + A[L] + A[R]
            current_abs = abs(current_sum)

            if current_abs < min_abs:
                min_abs = current_abs
                result = [A[i], A[L], A[R]]

                if min_abs == 0:
                    print(*result)
                    return

            # 5. 포인터 이동
            if current_sum < 0:
                L += 1
            else:
                R -= 1
    print(*result)

if __name__ == "__main__":
    solve()