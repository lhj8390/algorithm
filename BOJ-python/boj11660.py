if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [[0] * (n + 1)] * (n + 1)
    result = 0
    for i in range(n):
        data[i] = list(map(int, input().split()))

    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 - 1, x2):
        if x == (x1 - 1):
            result += sum(data[x][y1 - 1:])
        elif x == x2:
            result += sum(data[x][:y2])
        else:
            result += sum(data[x])

    print(result)