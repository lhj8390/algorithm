if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort()

    cnt = 0
    max_num = 0
    for a in arr:
        conf = [False] * 2 ** 31 - 1

        for el in a:
            if not conf[el]:
                conf[el] = True

        print(conf)
