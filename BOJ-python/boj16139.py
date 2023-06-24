if __name__ == '__main__':
    s = list(input())
    q = int(input())

    for i in range(q):
        a, l, r = map(str, input().split())
        s1 = s[int(l):int(r) + 1]
        print(s1.count(a))
