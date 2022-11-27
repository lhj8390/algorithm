def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = int(input())

    m = factorial(n)
    cnt = 0

    while m % 10 == 0:
        m = m // 10
        cnt += 1

    print(cnt)

