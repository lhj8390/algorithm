if __name__ == '__main__':
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    min_height, max_height = 1, max(heights)

    while min_height <= max_height:
        mid = (min_height + max_height) // 2
        height = 0
        for h in heights:
            if h > mid:
                height += (h - mid)

        if height >= m:
            min_height = mid + 1
        else:
            max_height = mid - 1

    print(max_height)