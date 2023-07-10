import sys
import string

if __name__ == '__main__':
    input = sys.stdin.readline
    s = list(input())
    q = int(input())

    result = {}
    for k in string.ascii_lowercase:
        result[ord(k)] = [0]
        count = 0
        for i in range(len(s)):
            if s[i] == k:
                count += 1
            result[ord(k)].append(count)

    for i in range(q):
        a, l, r = map(str, input().split())
        l, r = int(l), int(r)
        print(result[ord(a)][r + 1] - result[ord(a)][l])
