if __name__ == '__main__':
    x = int(input())
    y = x - 1
    z = 0
    while True:
        if y - 6 * z <= 0:
            print(z + 1)
            break
        y = y - 6 * z
        z += 1

