
if __name__ == '__main__':
    a = list(map(int, input().split()))
    result = list()
    index = 0
    for b in [1, 1, 2, 2, 2, 8]:
        result.append(str(b - a[index]))
        index += 1
    print(" ".join(result))
