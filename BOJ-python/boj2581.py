if __name__ == '__main__':
    m = int(input())
    n = int(input())
    num = list(range(m, n + 1))

    for x in range(m, n + 1):
        if x == 1:
            num.remove(x)
        for i in range(2, x):
            if x % i == 0:
                num.remove(x)
                break
    if len(num) == 0:
        print(-1)
    else:
        print(sum(num))
        print(min(num))