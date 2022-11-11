import math
if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance == 0:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        else:
            if distance == r1 + r2 or distance == abs(r2 - r1):  # 외접, 내접
                print(1)
            elif abs(r2 - r1) < distance < r1 + r2:  # 두 점에서 만날 때
                print(2)
            else:
                print(0)

