if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    result = 0
    time = 0
    for a in arr:
        time += a
        result += time
    print(result)