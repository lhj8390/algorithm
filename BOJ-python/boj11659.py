import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    sums = [0] * (n + 1)
    sums[0] = arr[0]
    for i in range(1, n):
        sums[i] = sums[i - 1] + arr[i]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(sums[j - 1] - sums[i - 2])
