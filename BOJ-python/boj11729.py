def hanoi(num, start, end, middle):
    if num == 1:
        print(start, end)
        return

    hanoi(num - 1, start, middle, end)
    print(start, end)
    hanoi(num - 1, middle, end, start)


if __name__ == '__main__':
    n = int(input())
    print(2**n - 1)
    hanoi(n, 1, 3, 2)




