import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    chess = []
    for _ in range(n):
        chess.append(map(int, input().split()))

    result = [0] * (n + 1)

    # 생각하는 알고리즘
    # 1. W인지 B인지 체크
    # 2. 누적합을 사용해서 B의 개수 누적으로 체크
    # 3. 구간을 정해서 B의 합 체크
    # 4. 최솟값 확인
