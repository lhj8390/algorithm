import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        cnt = 0
        for _ in range(n):
            cx, cy, r = map(int, input().split())

            distance_f = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
            distance_l = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
            if distance_f < r and distance_l < r:
                pass
            elif distance_f < r:
                cnt += 1
            elif distance_l < r:
                cnt += 1

        print(cnt)

