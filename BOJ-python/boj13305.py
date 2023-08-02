if __name__ == '__main__':
    n = int(input())
    dist = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    min_price = min(prices[:len(prices) - 1])
    price = 0
    for idx, d in enumerate(dist):
        if prices[idx] == min_price:
            price += sum(dist[idx:]) * prices[idx]
            break
        else:
            price += d * prices[idx]

    print(price)
