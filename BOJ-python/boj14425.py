if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set()
    b = list()
    for _ in range(n):
        a.add(input())

    for _ in range(m):
        b.append(input())

    diff = a & set(b)
    cnt = 0
    for d in diff:
        cnt += b.count(d)

    print(cnt)



