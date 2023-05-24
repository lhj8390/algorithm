from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    arr = [[] * n] * n
    for i in range(n):
        r, g, b = map(int, input().split())
        arr[i] = [r, g, b]

    print(arr)
    per = list(permutations([arr[i] for i in range(n)], n))
    print(per)

