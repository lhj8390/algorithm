def logic(a, b, n):
    global white, blue
    color = arr[a][b]
    for i in range(a, a + n):
        for j in range(b, b + n):
            if color != arr[i][j]:
                logic(a, b, n // 2)  # 1사분면
                logic(a, b + n // 2, n // 2)  # 2사분면
                logic(a + n // 2, b, n // 2)  # 3사분면
                logic(a + n // 2, b + n // 2, n // 2)  # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        sub = list(map(int, input().split()))
        arr.append(sub)

    white = 0
    blue = 0
    logic(0, 0, n)

    print(white)
    print(blue)
