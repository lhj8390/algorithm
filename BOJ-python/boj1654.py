if __name__ == '__main__':
    k, n = map(int, input().split())
    line = []
    for _ in range(k):
        line.append(int(input()))

    # 최대 랜선의 길이를 구하려면
    # 구할 수 있는 N 개의 랜선에 대한 최솟값 구하기

    min_num = sum(line) // n


