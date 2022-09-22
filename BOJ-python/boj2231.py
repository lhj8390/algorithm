if __name__ == '__main__':
    n = int(input())
    result = 0
    for t in range(1, n):
        sums = sum(map(int, str(t)))
        if sums + t == n:
            result = t
            break

    print(result)
