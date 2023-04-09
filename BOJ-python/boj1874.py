if __name__ == '__main__':
    n = int(input())
    stack = []
    result = []
    count = 1
    chk = True
    for _ in range(n):
        m = int(input())

        while m >= count:
            stack.append(count)
            result.append('+')
            count += 1

        if stack[-1] == m:
            stack.pop()
            result.append('-')
        else:
            chk = False
            break

    if chk:
        print('\n'.join(result))
    else:
        print('NO')


