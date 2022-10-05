import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    card = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    count = list(map(int, sys.stdin.readline().split()))

    result = {}
    for c in card:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    print(*[result[i] if i in result else 0 for i in count])
