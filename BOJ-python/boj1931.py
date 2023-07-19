if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: (x[1], x[0]))

    end = 0
    cnt = 0
    for start, finish in arr:
        if end <= start:
            cnt += 1
            end = finish

    print(cnt)
