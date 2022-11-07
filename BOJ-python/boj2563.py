if __name__ == '__main__':
    num = int(input())
    arr = [[0 for i in range(100)] for j in range(100)]
    sums = 0

    for _ in range(num):
        x, y = map(int, input().split())
        for a in range(x, x + 10):
            for b in range(y, y + 10):
                arr[a][b] = 1

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                sums += 1

    print(sums)



