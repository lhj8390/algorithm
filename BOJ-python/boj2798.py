from itertools import combinations
if __name__ == '__main__':
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    sums = list()

    for c in combinations(num, 3):
        if m >= c[0] + c[1] + c[2]:
            sums.append(c[0] + c[1] + c[2])

    sums.sort()
    sums.reverse()
    print(sums[0])





