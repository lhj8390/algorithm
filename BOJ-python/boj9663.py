# 퀸 자리가 맞는지 체크
# 행은 같을 수 없다.
def is_valid(r):
    for i in range(r):
        # 열이 같은지 체크
        if rows[i] == rows[r]:
            return False
        # 대각선 체크
        if abs(r - i) == abs(rows[r] - rows[i]):
            return False
    return True


# r행에 퀸 놓기
def dfs(r):
    global answer
    if r == n:
        answer += 1
        return

    for i in range(n):
        rows[r] = i
        if is_valid(r):
            dfs(r + 1)  # 다음 행에 퀸 놓기


if __name__ == '__main__':
    n = int(input())
    answer = 0
    rows = [0] * n
    dfs(0)
    print(answer)
