def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if data[a][b][c]:
        return data[a][b][c]

    if a < b < c:
        data[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        data[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return data[a][b][c]


if __name__ == '__main__':
    data = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break

        print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))
