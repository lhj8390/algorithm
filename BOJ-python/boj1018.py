if __name__ == '__main__':
    n, m = map(int, input().split())
    board = list()
    repair = list()

    for _ in range(n):
        board.append(input())

    for i in range(n - 7):
        for j in range(m - 7):
            first_w = 0
            first_b = 0
            for a in range(i, i + 8):
                for b in range(j, j + 8):
                    if (a + b) % 2 == 0:
                        if board[a][b] != 'W':
                            first_w += 1
                        elif board[a][b] != 'B':
                            first_b += 1
                    else:
                        if board[a][b] != 'W':
                            first_b += 1
                        elif board[a][b] != 'B':
                            first_w += 1
            repair.append(min(first_w, first_b))

    print(min(repair))