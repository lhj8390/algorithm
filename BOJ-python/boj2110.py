if __name__ == '__main__':
    n, c = map(int, input().split())
    coord = []
    diff = []
    for i in range(n):
        coord.append(int(input()))

    coord.sort()
    for i in range(1, len(coord)):
        diff.append(coord[i] - coord[i - 1])

    print(diff)