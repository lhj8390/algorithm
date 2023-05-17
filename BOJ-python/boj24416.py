def fib(n):
    global count_fib
    if n == 1 or n == 2:
        return 1
    else:
        count_fib += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global count_fibonacci
    f = [1] * (n + 1)

    for i in range(3, n + 1):
        count_fibonacci += 1
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


if __name__ == '__main__':
    n = int(input())
    count_fib, count_fibonacci = 1, 0

    fib(n)
    fibonacci(n)

    print(count_fib, count_fibonacci)
