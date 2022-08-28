if __name__ == '__main__':
    a = input()
    b = '0' + a if int(a) < 10 else a

    count = 0

    while True:
        y = int(b[0]) + int(b[1])
        x = b[1]
        b = x + str(y % 10)
        count += 1
        if int(a) == int(b):
            break

    print(count)
