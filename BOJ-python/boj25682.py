import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    data = []

    for _ in range(n):
        data.append(list(input().rstrip()))

    result = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i + j) % 2 == 0:  # B로 시작 해야 할 때
                if data[i - 1][j - 1] == 'B':
                    result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1]
                else:  # B 가 아닐 경우
                    result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1] + 1

            else:  # w로 시작 해야 할 때
                if data[i - 1][j - 1] == 'W':
                    result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1]
                else:  # B 가 아닐 경우
                    result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1] + 1

    max_num = -sys.maxsize
    min_num = sys.maxsize
    for r in range(k, n + 1):
        for c in range(k, m + 1):
            max_num = max(result[r][c] - result[r - k][c] - result[r][c - k] + result[r - k][c - k], max_num)
            min_num = min(result[r][c] - result[r - k][c] - result[r][c - k] + result[r - k][c - k], min_num)

    print(min(min_num, max_num, k * k - min_num, k * k - max_num))  # B로 시작 또는 W로 시작 체크

