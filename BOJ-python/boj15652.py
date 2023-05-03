import itertools

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = [i for i in range(1, n + 1)]

    # 중복 조합 구현 시에는 combinations_with_replacement 사용
    result = itertools.combinations_with_replacement(arr, m)

    for r in result:
        print(' '.join(map(str, r)))
