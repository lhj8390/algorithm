if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # 끝나는 시간이 제일 적은 순
    arr.sort(key=lambda x: (x[1], x[0]))

    end = 0
    cnt = 0
    for start, finish in arr:
        # 끝나는 시간이 다음 시작 시간 보다 작을 경우
        if end <= start:
            cnt += 1
            end = finish

    print(cnt)
