if __name__ == '__main__':
    n = int(input())
    arr = [[0] * (n + 1)] * (n + 1)

    for i in range(n):
        ele = list(map(int, input().split()))
        arr[i] = ele

    for i in range(1, len(arr)):
        for idx in range(len(arr[i])):
            # 첫번째 열
            if idx == 0:
                arr[i][idx] = arr[i - 1][idx] + arr[i][idx]
            # 마지막 열
            elif idx == i:
                arr[i][idx] = arr[i - 1][idx - 1] + arr[i][idx]
            else:
                arr[i][idx] = max(arr[i - 1][idx - 1], arr[i - 1][idx]) + arr[i][idx]

    print(max(arr[n]))
