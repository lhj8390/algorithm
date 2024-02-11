def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:  # 정렬이 맞을 경우
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq


if __name__ == '__main__':
    seq = [7, 3, 6, 1]
    assert gnome_sort(seq) == sorted(seq)
    print("테스트 통과")
