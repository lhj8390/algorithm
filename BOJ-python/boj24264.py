"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j];
    return sum;
}
수행 횟수 체크
"""

if __name__ == '__main__':
    n = int(input())

    # 1부터 n까지 loop 를 2번 돌기 때문에 수행 횟수는 n * n 이 된다.
    print(n * n)
    # 최고차항의 차수 무조건 2
    print(2)
