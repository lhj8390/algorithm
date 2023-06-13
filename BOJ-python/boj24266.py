"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k];
    return sum;
}
수행 횟수 체크
"""


if __name__ == '__main__':
    n = int(input())

    #  n 의 3 제곱
    print(n ** 3)
    # # 최고차항의 차수 무조건 3
    print(3)
