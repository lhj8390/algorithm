import math
global cnt


def merge_sort(a):
    if len(a) > 1:
        q = math.ceil(len(a) / 2)
        return merge(merge_sort(a[:q]), merge_sort(a[q:]))
    else:
        return a


def merge(left, right):
    tmp = []
    idx1, idx2 = 0, 0
    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] <= right[idx2]:
            tmp.append(left[idx1])
            idx1 += 1
        else:
            tmp.append(right[idx2])
            idx2 += 1
    while idx1 < len(left):
        tmp.append(left[idx1])
        idx1 += 1
    while idx2 < len(right):
        tmp.append(right[idx2])
        idx2 += 1

    for t in tmp:
        cnt.append(t)
    return tmp


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = []
    merge_sort(a)
    if k <= len(cnt):
        print(cnt[k - 1])
    else:
        print(-1)
