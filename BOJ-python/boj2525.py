if __name__ == '__main__':
    a, b = map(int, input().split())
    c = int(input())

    if b + c < 60:
        print(a, b + c)
    else:
        h = (b + c) // 60
        if a + h >= 24:
            print((a + h) - 24, (b + c) % 60)
        else:
            print(a + h, (b + c) % 60)
