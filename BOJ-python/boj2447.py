def star(s):
    if s == 3:
        return ["***", "* *", "***"]

    arr = star(s // 3)
    stars = list()
    for i in arr:
        stars.append(i * 3)
    for i in arr:
        stars.append(i + " " * (s // 3) + i)
    for i in arr:
        stars.append(i * 3)

    return stars


if __name__ == '__main__':
    n = int(input())

    print("\n".join(star(n)))