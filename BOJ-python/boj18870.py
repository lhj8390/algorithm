import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    rank = sorted(set(num))

    rank_dic = {rank[i]: i for i in range(len(rank))}

    print(*[rank_dic[m] for m in num])

