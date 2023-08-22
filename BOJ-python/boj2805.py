if __name__ == '__main__':
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    min_height, max_height = 1, max(heights)

    # 이분탐색 수행
    while min_height <= max_height:
        mid = (min_height + max_height) // 2  # 중간 길이 찾기
        height = 0
        for h in heights:
            if h > mid:
                height += (h - mid)  # 중간 길이로 나무를 자른 뒤 높이 구하기

        if height >= m:  # M미터 이상일 경우 최소 높이 증가
            min_height = mid + 1
        else:  # M미터 미만일 경우 최대 높이 감소
            max_height = mid - 1

    print(max_height)