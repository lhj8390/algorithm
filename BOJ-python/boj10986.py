if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if sum(arr[i:j + 1]) % m == 0:
                cnt += 1

    print(cnt)
