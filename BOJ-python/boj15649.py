if __name__ == '__main__':
    # Backtracking
    n, m = map(int, input().split())
    visited = [False] * n
    result = []


    def dfs():
        if len(result) == m:
            print(' '.join(map(str, result)))

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                result.append(i + 1)

                dfs()
                visited[i] = False
                result.pop()

    dfs()
