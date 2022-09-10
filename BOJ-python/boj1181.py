if __name__ == '__main__':
    n = int(input())
    word_dic = dict()

    i = 0
    for _ in range(n):
        word = input()
        word_dic[word] = len(word)
    sorted_dic = sorted(word_dic.items())

    for s in sorted(sorted_dic, key=lambda x: x[1]):
        print(s[0])
