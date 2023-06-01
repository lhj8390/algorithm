if __name__ == '__main__':
    n = int(input())
    # 0 ~ 10 까지 나열 -> 자릿수가 n 일 때, 서로 1 차이가 나는지 체크 하는 로직

    # ex) n = 2 일 때,
    # 0 1 2 3 4 5 6 7 8 9 (첫 번째 자리)
    # 0 1 2 3 4 5 6 7 8 9 (두 번째 자리)
    # 서로 비교
    arr = [[0 for i in range(10)] for j in range(n + 1)]

    for i in range(1, 10):  # n = 1 일 때
        arr[1][i] = 1
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:  # 0 일 때, 1만 계단 수
                arr[i][j] = arr[i - 1][1]
            elif j == 9:  # 9일 때, 8만 계단 수
                arr[i][j] = arr[i - 1][8]
            else:  # 나머지 : +1, -1 계단 수
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j + 1]
    print(sum(arr[n]) % 1000000000)


