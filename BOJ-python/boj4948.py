if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        num = [False, False] + [True] * (2 * n - 1)

        for i in range(2, n + 1):
            if num[i]:
                for x in range(2 * i, 2 * n + 1, i):
                    num[x] = False

        print(len([y for y in range(2 * n + 1) if num[y] and y > n]))
