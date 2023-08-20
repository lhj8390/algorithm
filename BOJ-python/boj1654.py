if __name__ == '__main__':
    k, n = map(int, input().split())
    line = []
    for _ in range(k):
        line.append(int(input()))

    min_val, max_val = 1, max(line)

    # 랜선의 길이를 움직여 개수와 맞는지 체크
    while min_val <= max_val:  # 랜선의 길이 찾기
        mid = (min_val + max_val) // 2  # 이진 탐색을 위해 중간값 찾기
        cnt = 0  # 랜선 수
        for li in line:
            cnt += li // mid  # 중간 값으로 랜선이 몇개 생기는 지 카운트

        if cnt >= n:  # 양이 초과할 경우 최소 랜선 길이 갱신
            min_val = mid + 1
        else:  # 양이 부족할 경우 최대 랜선 길이 갱신
            max_val = mid - 1

    print(max_val)
