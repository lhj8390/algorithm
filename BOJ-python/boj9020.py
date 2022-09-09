if __name__ == '__main__':
    t = int(input())

    num = [False, False] + [True] * 9999

    for i in range(2, 10001):
        if num[i]:
            for j in range(2 * i, 10001, i):
                num[j] = False
    cnt = 0
    while cnt < t:

        n = int(input())
        a = n // 2
        for x in range(a, 1, -1):
            if num[n - x] and num[x]:
                print(x, n - x)
                break

        cnt += 1
