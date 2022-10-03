import sys
if __name__ == '__main__':
    n, m = map(int, input().split())
    dic = dict()
    result = list()

    for i in range(n):
        a = sys.stdin.readline().strip()
        dic[i + 1] = a
        dic[a] = i + 1

    for _ in range(m):
        b = sys.stdin.readline().strip()
        if b.isdigit():
            result.append(dic[int(b)])
        else:
            result.append(str(dic[b]))

    print("\n".join(result))





