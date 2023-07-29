if __name__ == '__main__':
    data = input()
    # 괄호가 없는 식의 최솟값을 구하기 위해서는
    # "-" 를 기준으로 괄호를 쳤을 경우를 구하면 된다.
    # ("-" 뒤의 값의 합은 무조건 음수)
    data = data.split('-')

    sums = 0
    # "-" 를 기준으로 앞 부분
    for d in data[0].split('+'):
        sums += int(d)

    # "-" 를 기준으로 뒤의 부분
    # d 변수 에는 "-" 로 split 한 각각의 배열이 들어가 있다.
    # 따라서 + 여부만 체크 하면 된다.
    for d in data[1:]:
        for d2 in d.split('+'):
            sums -= int(d2)

    print(sums)
