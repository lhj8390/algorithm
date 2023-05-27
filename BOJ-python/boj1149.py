if __name__ == '__main__':
    n = int(input())
    arr = [[0] * n] * n
    for i in range(n):
        r, g, b = map(int, input().split())
        arr[i] = [r, g, b]

    # depth 1 : 26(r), 40(g), 83(b)
    # depth 2 : r 값, depth 1의 (b), depth 1의 (g)
    # depth n : r[n] 값, depth n-1의 (b), depth n-1의 (g)
    for i in range(1, len(arr)):
        # r을 선택할 경우
        arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
        # g를 선택할 경우
        arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
        # b를 선택할 경우
        arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

    print(min(arr[n - 1][0], arr[n - 1][1], arr[n - 1][2]))