def cantor(arr):
    s = len(arr) // 3
    if len(arr) == 1:
        print(*arr, end='')
        return

    split_data = ([arr[i:i + s] for i in range(0, len(arr), s)])

    for idx in range(s):
        split_data[1][idx] = " "

    for i in range(3):
        cantor(split_data[i])


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            cantor(["-" for _ in range(3 ** n)])
            print()

        except:
            break
