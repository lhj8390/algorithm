# 부분합 문제
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sums = [0] * (n + 1)  # 부분합 배열
    cnt_arr = [0] * (m + 1)  # 나머지가 같은 것 끼리 카운트
    for i in range(1, n ):
        sums[i] += (sums[i - 1] + arr[i]) % m
        cnt_arr[sums[i]] += 1

    print(sum(cnt_arr))
