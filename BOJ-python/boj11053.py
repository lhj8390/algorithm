if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    result = [1] * (n + 1)

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                result[i] = max(result[i], result[j] + 1)

    print(max(result))