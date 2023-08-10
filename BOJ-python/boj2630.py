# 모든 칸이 같은 색이 될 때까지 분할하는 문제
def logic(a, b, n):
    global white, blue
    color = arr[a][b] # 현재 색깔 (하얀색 or 파란색)
    for i in range(a, a + n):
        for j in range(b, b + n):
            # 현재 색상과 같지 않을 경우 분할한다.
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
