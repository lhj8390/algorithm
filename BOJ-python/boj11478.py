if __name__ == '__main__':
    s = input()
    n = len(s)
    result = set()

    for i in range(1, n + 1):           # 문자열 길이
        for j in range(n + 1 - i):      # 자리
            result.add(s[j:j + i])

    print(len(result))