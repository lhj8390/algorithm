if __name__ == '__main__':
    a = int(input())
    b = input()
    b1, b2, b3 = b[2], b[1], b[0]

    c = a * int(b1)
    d = a * int(b2)
    e = a * int(b3)

    print(c, d, e, a * int(b), sep='\n')

