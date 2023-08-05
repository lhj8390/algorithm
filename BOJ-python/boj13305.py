import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    dist = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    min_price = sys.maxsize
    price = 0
    for i in range(n - 1):
        # 거리를 이동하면서 최솟값 구하기
        if prices[i] < min_price:
            # 최솟값을 찾았을 경우 갱신
            min_price = prices[i]
        # 최솟값에 거리 값을 곱하는게 제일 최소의 비용
        price += min_price * dist[i]

    print(price)
