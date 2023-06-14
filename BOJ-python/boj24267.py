"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k];
    return sum;
}
수행 횟수 체크
"""


if __name__ == '__main__':
    n = int(input())

    # nC3 = (n-2)(n-1)n / 6
    #  n 의 3 제곱
    print(n * (n - 1) * (n - 2) // 6)
    # # 최고차항의 차수 무조건 3
    print(3)
