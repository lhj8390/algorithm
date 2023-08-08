def logic(a, b):
    global white, blue
    if a == 1 or b == 1:
        white += 1
        blue += 1
        return
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                logic(i // 2, j // 2)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        sub = list(map(int, input().split()))
        arr.append(sub)

    white = 0
    blue = 0
    logic(n, n)

    print(white)
    print(blue)
