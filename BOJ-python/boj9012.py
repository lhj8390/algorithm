if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        vps = input()

        if len(vps) % 2 != 0:
            print('NO')
            continue

        chk = 0
        for v in vps:
            if v == '(':
                chk += 1
            else:
                chk -= 1
            if chk < 0:
                print('NO')
                break

        if chk == 0:
            print('YES')
        elif chk > 0:
            print('NO')
