def han(n):
    num = list(str(n))
    diff = int(num[0]) - int(num[1])

    for i in range(len(num) - 1):
        if int(num[i + 1]) != int(num[i]) - diff:
            return False
    return True


if __name__ == '__main__':
    x = int(input())
    count = x if x < 100 else 99
    for a in range(100, x + 1):
        if han(a):
            count += 1

    print(count)
