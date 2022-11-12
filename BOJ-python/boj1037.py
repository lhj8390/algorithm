if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    if n % 2 == 1:
        print(arr[n // 2] ** 2)
    else:
        print(arr[(n // 2) - 1] * arr[(n // 2)])
