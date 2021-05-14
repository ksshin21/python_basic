#43일차 덧셈뺄셈 합계(3/4) - 1차 시도 (KS)
# 1-2+3-4+5 ... n 의 합계 구하기
# -1을 곱해 부호를 바꾸어 더하는 알고리즘
# 부호 변수명 sign 반복문 카운터 i
print("덧셈 뺄셈 합계 (3/4)")
while 1:
    n = int(input("n : "))
    if n == 0:      # 입력값이 0이면 종료
        break
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sign = -1
        else:
            sign = 1
        isign = i * sign
        sum += isign
        print('sign=%2d i*sign= %d'%(sign, isign))
    print(f'합계 : {sum}')
