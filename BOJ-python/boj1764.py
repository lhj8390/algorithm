if __name__ == '__main__':
    n, m = map(int, input().split())
    not_listen = set()
    not_show = set()
    for _ in range(n):
        not_listen.add(input())
    for _ in range(m):
        not_show.add(input())

    result = list(not_listen & not_show)
    result.sort()

    print(len(result))
    print("\n".join(result))