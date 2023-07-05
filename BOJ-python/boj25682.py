import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    chess = []

    # 생각하는 알고리즘
    # 1. W인지 B인지 체크
    # 2. 누적합을 사용해서 B의 개수 누적으로 체크
    # 3. 구간을 정해서 B의 합 체크
    # 4. 최솟값 확인

    for _ in range(n):
        data = input()
        parsed = []
        for d in data:
            if d == "W":
                parsed.append(1)
            else:
                parsed.append(0)
        chess.append(parsed)

    print(chess)

    result = [[0] * (n + 1) for _ in range(m + 1)]
    print(result)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result[i][j] = result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1] + chess[i - 1][j - 1]

    print(result)

