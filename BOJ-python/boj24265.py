"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
수행 횟수 체크
"""


if __name__ == '__main__':
    n = int(input())

    # n = 7 일 때,
    # 첫번 째 반복 문이 1 이면 6
    # 첫번 째 반복 문이 2 이면 5
    # .... 첫번 째 반복 문이 6이면 1
    # 즉, 6 + 5 + 4 + 3 + 2 + 1 = n(n - 1) / 2 = 21
    print(n * (n - 1) // 2)
    # # 최고차항의 차수 무조건 2
    print(2)
