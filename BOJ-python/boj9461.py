def p(n):
    if n == 1 or n == 2 or n == 3:
        return arr[n]

    for i in range(4, n + 1):
        arr[i] = arr[i - 2] + arr[i - 3]

    return arr[n]


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [1] * 101
        print(p(n))
