import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    dist = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    min_price = sys.maxsize
    price = 0
    for i in range(n - 1):
        if prices[i] < min_price:
            min_price = prices[i]
        price += min_price * dist[i]

    print(price)
