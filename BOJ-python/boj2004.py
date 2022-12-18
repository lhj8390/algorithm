def num_cnt(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())

    five_count = num_cnt(n, 5) - num_cnt(m, 5) - num_cnt(n - m, 5)
    two_count = num_cnt(n, 2) - num_cnt(m, 2) - num_cnt(n - m, 2)

    # 0의 갯수는 2의 지수와 5의 지수 중 작은 값
    answer = min(five_count, two_count)
    print(answer)
