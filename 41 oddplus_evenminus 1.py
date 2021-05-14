#41일차 덧셈뺄셈 합계(1/4) - 1차 시도 (KS)
# 1-2+3-4+5 ... n 의 합계 구하기
# 홀수이면 더하고 짝수이면 빼기
print("덧셈 뺄셈 합계 (1/4)")
while 1:
    n = int(input("n : "))
    if n == 0:      # 입력값이 0이면 종료
        break
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            print('%2d - %2d = '%(sum, i), end='')
            sum -= i
            print('%2d'%(sum))
        else:
            print('%2d + %2d = '%(sum, i), end='')
            sum += i
            print('%2d'%(sum))
    print(f'합계 : {sum}')
