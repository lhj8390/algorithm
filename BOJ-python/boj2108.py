from collections import Counter
import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    num = list()
    for _ in range(n):
        num.append(int(sys.stdin.readline()))
    num.sort()

    print(round(sum(num) / n))
    print(num[n // 2])

    cnt = Counter(num).most_common(2)
    if len(cnt) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])

    print(max(num) - min(num))

