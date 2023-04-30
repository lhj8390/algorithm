import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    for v in nums:
        print(1) if v in a else print(0)