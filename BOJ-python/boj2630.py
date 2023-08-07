if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        sub = list(map(int, input().split()))
        arr.append(sub)

    white = 0
    blue = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                white += 1
            else:
                blue += 1

    print(white)
    print(blue)
