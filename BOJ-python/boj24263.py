"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
수행 횟수 체크
"""

if __name__ == '__main__':
    n = int(input())

    # 1부터 n까지 loop 를 돌기 때문에 수행 횟수는 n 이 된다.
    print(n)
    print(1)
