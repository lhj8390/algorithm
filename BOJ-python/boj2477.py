if __name__ == '__main__':
    x = int(input())
    arr = list()
    max_width = 0
    max_height = 0
    w_direction = 0
    h_direction = 0

    for _ in range(6):
        arr.append(list(map(int, input().split())))

    idx = 0
    for r in arr:
        # 동쪽 or 서쪽
        if r[0] == 1 or r[0] == 2:
            if max_width < r[1]:
                max_width = r[1]
                w_direction = idx
        # 남쪽 or 북쪽
        else:
            if max_height < r[1]:
                max_height = r[1]
                h_direction = idx
        idx += 1

    min_width = abs(arr[(w_direction - 1) % 6][1] - arr[(w_direction + 1) % 6][1])
    min_height = abs(arr[(h_direction - 1) % 6][1] - arr[(h_direction + 1) % 6][1])
    print((max_width * max_height - min_width * min_height) * x)
