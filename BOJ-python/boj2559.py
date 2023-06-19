if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = [[0] * (n + 1)] * (n + 1)

    result[1] = arr
    for i in range(2, n):
        for j in range(n - i):
            result[i][j] = result[i - 1][j] + arr[i]

    print(result)