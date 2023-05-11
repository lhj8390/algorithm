import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    vocab = []
    cnt = dict()

    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        if len(word) < m:
            continue

        vocab.append(word)
        if cnt.get(word) is None:
            cnt[word] = 1
        else:
            cnt[word] += 1

    result = sorted(set(vocab), key=lambda x: (-cnt[x], -len(x), x))
    for r in result:
        print(r)
