def merge_sort(seq):
    """
    1) pop() 을 이용한 병합 정렬
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]  # 기존 배열을 반으로 쪼개기
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res


def merge_sort_sep(seq):
    """
    2) 두 함수로 나누어서 구현.
    한 함수에서는 배열을 나누고, 다른 함수에서는 배열 병합
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = merge_sort_sep(seq[:mid]), merge_sort_sep(seq[mid:])
    return merge(left, right)


def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result


if __name__ == '__main__':
    seq = [5, 3, 2, 6, 8, 1, 0, 3, 6, 7, 3]
    assert merge_sort(seq) == sorted(seq)
    assert merge_sort_sep(seq) == sorted(seq)
    print("테스트 통과!")