if __name__ == '__main__':
    n, c = map(int, input().split())
    coord = []
    diff = []
    for i in range(n):
        coord.append(int(input()))

    coord.sort()

    min_dist, max_dist = 1, coord[-1] - coord[0]

    result = 0
    while min_dist <= max_dist:
        mid = (min_dist + max_dist) // 2
        current = coord[0]
        cnt = 1
        for i in range(1, len(coord)):
            if coord[i] >= current + mid:
                cnt += 1
                current = coord[i]
        if cnt >= c:
            min_dist = mid + 1
            result = mid
        else:
            max_dist = mid - 1

    print(result)
