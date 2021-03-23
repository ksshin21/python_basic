# 14일차
# 1부터 n까지 홀수합 구하기
# 홀수합계 - 1차시도(KS)
while True:
    n = int(input('정수 n : '))
    if n == 0:
        break;
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            sum += i
    print('합계 : ', sum)
