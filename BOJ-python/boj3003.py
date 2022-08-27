
if __name__ == '__main__':
    a = list(map(int, input().split()))
    result = list()
    # part 1
    for idx, b in enumerate([1, 1, 2, 2, 2, 8]):
        result.append(str(b - a[idx]))
    print(" ".join(result))

    # part 2
    for i, j in zip(a, [1, 1, 2, 2, 2, 8]):
        print(j - i, end=' ')
