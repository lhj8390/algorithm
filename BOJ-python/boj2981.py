if __name__ == '__main__':
    n = int(input())

    arr = [int(input()) for _ in range(n)]
    arr.sort()
    result = set()

    # 최대 공약수 구하기
    gc = arr[1] - arr[0]
    for i in range(n - 1):
        x, y = gc, arr[i + 1] - arr[i]
        while y:
            x, y = y, x % y
        gc = x
    result.add(gc)

    # 최대 공약수 의 약수 구하기
    for g in range(2, int(gc ** 0.5) + 1):
        if gc % g == 0:
            result.add(g)
            result.add(gc // g)

    result = list(result)
    result.sort()
    print(*result)
