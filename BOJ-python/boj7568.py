if __name__ == '__main__':
    n = int(input())
    result = list()
    rank = list()
    for _ in range(n):
        x, y = map(int, input().split())
        result.append([x, y])

    for r in result:
        cnt = 1
        for i in result:
            if r[0] < i[0] and r[1] < i[1]:
                cnt += 1
        rank.append(str(cnt))

    print(" ".join(rank))