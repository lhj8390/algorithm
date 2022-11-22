def bino_coef(n, m):
    if n > m:
        return 0

    cache = [[-1 for _ in range(m + 1)] for _ in range(m + 1)]

    def choose(items, got):
        if items == m:
            return got == n

        if cache[items][got] != -1:
            return cache[items][got]

        cache[items][got] = choose(items + 1, got) + choose(items + 1, got + 1)
        return cache[items][got]

    return choose(0, 0)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        print(bino_coef(n, m))



