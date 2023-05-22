if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        # 현재 값을 최대 값으로 변경 -> 다음 로직 에서 max(현재 값, 이전 값 + 현재값)
        # 누적으로 max 값을 체크한다.
        arr[i] = max(arr[i], arr[i] + arr[i - 1])

    print(max(arr))