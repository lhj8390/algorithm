import sys


def dfs(depth, idx):
    global min_num

    start, link = 0, 0
    if depth == n // 2:
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start += arr[i][j]
                elif not visit[i] and not visit[j]:
                    link += arr[i][j]

        min_num = min(min_num, abs(start - link))
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(depth + 1, i + 1)
            visit[i] = False


if __name__ == '__main__':
    n = int(input())
    arr = [[0 for j in range(n)] for i in range(n)]
    visit = [False for _ in range(n)]
    min_num = sys.maxsize

    for i in range(n):
        arr[i] = list(map(int, input().split()))

    dfs(0, 0)
    print(min_num)
