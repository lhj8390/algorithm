if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        clothes = [input().split() for _ in range(n)]
        dic = dict()

        for c in clothes:
            if c[1] in dic:
                dic[c[1]] += 1
            else:
                dic[c[1]] = 1

        result = 1
        for d in dic.values():
            result *= d + 1

        print(result - 1)
