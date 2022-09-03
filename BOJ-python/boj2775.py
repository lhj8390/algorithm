if __name__ == '__main__':
    cnt = int(input())

    for i in range(cnt):
        k = int(input())  # 층
        n = int(input())  # 호

        # 0층의 사람들
        arr = [i for i in range(1, n + 1)]

        for x in range(k):
            result = list()
            for y in range(n):
                result.append(sum(arr[:y + 1]))
            arr = result
        print(arr[-1])
