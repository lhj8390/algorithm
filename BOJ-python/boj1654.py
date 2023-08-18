if __name__ == '__main__':
    k, n = map(int, input().split())
    line = []
    for _ in range(k):
        line.append(int(input()))

    min_val, max_val = 1, max(line)

    while min_val <= max_val:
        mid = (min_val + max_val) // 2
        cnt = 0
        for li in line:
            cnt += li // mid

        if cnt >= n:
            min_val = mid + 1
        else:
            max_val = mid - 1

    print(max_val)
