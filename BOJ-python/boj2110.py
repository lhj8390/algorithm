if __name__ == '__main__':
    n, c = map(int, input().split())
    coord = []
    diff = []
    for i in range(n):
        coord.append(int(input()))

    coord.sort()
    for i in range(1, len(coord)):
        diff.append(coord[i] - coord[i - 1])

    min_dist, max_dist = 1, max(diff)

    while min_dist <= max_dist:
        mid = (min_dist + max_dist) // 2
        max_diff = 0
        for c in coord:
            if max_diff < mid:
