if __name__ == '__main__':
    data = input()
    data = data.split('-')

    sums = 0
    for d in data[0].split('+'):
        sums += int(d)

    for d in data[1:]:
        for d2 in d.split('+'):
            sums -= int(d2)

    print(sums)
