def self_num(n):
    number = n
    for i in list(str(n)):
        number += int(i)
    return number


if __name__ == '__main__':
    a = list(range(1, 10000))
    s = set()

    for x in range(1, 10000):
        if self_num(x) < 10000:
            s.add(self_num(x))

    for s1 in s:
        if s1 in a:
            a.remove(s1)

    print(*a, sep='\n')
