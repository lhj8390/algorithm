if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.reverse()

    cnt = 0
    for a in arr:
        # if k % a == 0:
        #     break
        if k // a < 10:
            cnt += k // a
            k = k - (k // a) * a

    print(cnt)
