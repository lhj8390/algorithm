if __name__ == '__main__':
    n = int(input())
    stair = [0] * (n + 1)
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        stair[i] = int(input())

    for i in range(1, n + 1):
        if i == 1:
            result[i] = stair[i]
        elif i == 2:
            result[i] = stair[i - 1] + stair[i]
        elif i == 3:
            result[i] = max(stair[i - 2] + stair[i], stair[i - 1] + stair[i])
        else:
            result[i] = max(result[i - 3] + stair[i - 1] + stair[i], result[i - 2] + stair[i])

    print(result[n])
