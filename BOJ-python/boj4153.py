if __name__ == '__main__':
    while True:
        sides = list(map(int, input().split()))
        sides.sort()
        if sum(sides) == 0:
            break
        else:
            if sides[0]**2 + sides[1]**2 == sides[2]**2:
                print('right')
            else:
                print('wrong')

