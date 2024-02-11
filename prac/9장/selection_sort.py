def selection_sort(seq):
    length = len(seq)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if seq[min_index] > seq[j]:
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq


if __name__ == '__main__':
    seq = [11, 3, 27, 25, 2, 6, 9, 18]
    assert selection_sort(seq) == sorted(seq)
    print("테스트 통과")
