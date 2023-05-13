def dfs(idx):
    global result
    global max_num, min_num
    if idx == n:
        if result > max_num:
            max_num = result
        if result < min_num:
            min_num = result
        return

    for i in range(4):
        tmp = result
        if op_lst[i] > 0:
            if i == 0:
                result += lst[idx]
            elif i == 1:
                result -= lst[idx]
            elif i == 2:
                result *= lst[idx]
            else:
                if result >= 0:
                    result //= lst[idx]
                else:
                    result = (-result // lst[idx] * -1)

            op_lst[i] -= 1
            dfs(idx + 1)
            result = tmp
            op_lst[i] += 1


if __name__ == '__main__':
    max_num = -int(1e9)
    min_num = int(1e9)

    n = int(input())
    lst = list(map(int, input().split()))
    op_lst = list(map(int, input().split()))

    result = lst[0]

    dfs(1)

    print(max_num)
    print(min_num)
