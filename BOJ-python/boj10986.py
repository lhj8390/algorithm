# 부분합 문제
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sums = [0] * (n + 1)  # 부분합 배열
    cnt_arr = [0] * (m + 1)  # 나머지가 같은 것 끼리 카운트
    for i in range(1, n + 1):
        sums[i] += (sums[i - 1] + arr[i - 1]) % m
        cnt_arr[sums[i]] += 1

    cnt = cnt_arr[0]  # 나머지가 0 인 경우는 2개의 수를 뽑지 않아도 나누어 떨어진다.
    for c in cnt_arr:  # 나머지가 같을 경우 2개의 수 조합 (cC2)
        cnt += c * (c - 1) // 2
    print(cnt)
