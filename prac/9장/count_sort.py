from collections import defaultdict


def count_sort_dict(seq):
    arr, dic = [], defaultdict(list)
    for i in seq:
        dic[i].append(i)
    for k in range(min(dic), max(dic) + 1):  # 최소와 최대를 구해 숫자를 직접 배치
        arr.extend(dic[k])
    return arr


if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 9, 3, 5, 6, 2, 6, 4, 1, 5, 3]
    assert count_sort_dict(seq) == sorted(seq)
    print("테스트 통과")