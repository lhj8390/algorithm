if __name__ == '__main__':
    n = int(input())

    arr = [0] * (n + 1)

    # 10 -> 9 -> 3 -> 1
    # 9 -> 3 -> 1
    # 3 -> 1
    # 앞에서 구한 결과를 저장 했다가 후에 사용 한다.
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i], arr[i // 2] + 1)  # 계산한 횟수 저장
        if i % 3 == 0:
            arr[i] = min(arr[i], arr[i // 3] + 1)  # 계산한 횟수 저장

    print(arr[n])
