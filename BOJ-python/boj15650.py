import itertools

if __name__ == '__main__':
    n, m = map(int, input().split())

    data = [i for i in range(1, n + 1)]

    for a in itertools.combinations(data, m):
        print(' '.join(map(str, a)))