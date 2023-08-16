if __name__ == '__main__':
    k, n = map(int, input().split())
    line = []
    for _ in range(k):
        line.append(int(input()))

    line.sort()
    div_num = 2
    # 개수가 n이 될 때까지 반복
    while True:
        tmp = 0
        for li in line:
            tmp += li // div_num

        if tmp == n:
            break
        else:
            div_num += 1
