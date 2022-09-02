if __name__ == '__main__':
    x = int(input())

    max_size = 1
    i = 0
    num = list()
    while i < x:
        i += max_size
        max_size += 1
    max_size -= 1
    a = 1 if max_size % 2 == 0 else max_size
    b = max_size if max_size % 2 == 0 else 1

    for n in range(max_size):
        num.append(f'{a}/{b}')
        if max_size % 2 == 0:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1

    print(num[x - (i - max_size) - 1])
