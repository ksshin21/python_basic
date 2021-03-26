# 16일차 
# 1부터 n까지 홀수, 짝수, 총합계 구하기
# 홀수, 짝수, 총합계 - 1차시도(KS)
while True:
    n = int(input('정수 n : '))
    if n == 0:
        break;
    odd = 0
    even = 0
    total = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            odd += i
        else:
            even += i
    total = odd + even
    print('홀수합계 : ', odd)
    print('짝수합계 : ', even)
    print('총합계 : ', total)
