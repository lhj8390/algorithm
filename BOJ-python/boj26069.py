
if __name__ == '__main__':
    n = int(input())
    chong = set()
    chong.add("ChongChong")

    for _ in range(n):
        a, b = map(str, input().split())

        if a in chong or b in chong:
            chong.add(a)
            chong.add(b)

    print(len(chong))