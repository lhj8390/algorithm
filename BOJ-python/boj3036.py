if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, len(arr)):
        x = arr[0]
        y = arr[i]
        while y:
            x, y = y, x % y

        gcd = x

        print('{}/{}'.format(arr[0] // gcd, arr[i] // gcd))

