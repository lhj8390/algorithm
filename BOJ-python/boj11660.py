import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    data = [[0] * (n + 1)] * (n + 1)
    for i in range(n):
        data[i] = list(map(int, input().split()))

    result = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1] + data[i - 1][j - 1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        print(result[x2][y2] - result[x1 - 1][y2] - result[x2][y1 - 1] + result[x1 - 1][y1 - 1])