
if __name__ == '__main__':
    n = int(input())
    join = set()
    cnt = 0

    for _ in range(n):
        word = input()
        if word == "ENTER":
            cnt += len(join)
            join.clear()
        else:
            join.add(word)
    print(len(join) + cnt)