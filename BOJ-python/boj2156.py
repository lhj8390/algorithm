if __name__ == '__main__':
    n = int(input())
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(input())

    result = [0] * (n + 2)
    result[1] = arr[1]
    result[2] = result[1] + arr[2]
    for i in range(3, n + 1):
        result[i] = max(result[i - 3] + arr[i - 1] + arr[i], result[i - 2] + arr[i], result[i - 1])

    print(result[n])
