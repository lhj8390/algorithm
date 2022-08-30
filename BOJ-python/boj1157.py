if __name__ == '__main__':
    n = input().lower()
    s = set(n)
    c = list()

    for i in s:
        c.append(n.count(i))

    if c.count(max(c)) > 1:
        print('?')
    else:
        s2 = list(s)
        print(s2[c.index(max(c))].upper())
