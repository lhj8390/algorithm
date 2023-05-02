import itertools

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = [i for i in range(1, n + 1)]

    # 중복 순열 구현 시에는 product 사용
    result = itertools.product(arr, repeat=m)
    for r in result:
        print(' '.join(map(str, r)))
