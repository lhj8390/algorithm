if __name__ == '__main__':
    m, n = map(int, input().split())

    a = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if a[i]:
            for j in range(i * 2, n + 1, i):
                a[j] = False
    for i, j in enumerate(a):
        if j and i >= m:
            print(i)
