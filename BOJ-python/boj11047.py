if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.reverse()

    cnt = 0
    for a in arr:
        if k // a > 0:
            cnt += k // a
            k = k % a

    print(cnt)
