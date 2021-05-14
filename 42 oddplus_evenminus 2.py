#42일차 덧셈뺄셈 합계(2/4) - 1차 시도 (KS)
# 1-2+3-4+5 ... n 의 합계 구하기
# 홀수의 합에서 짝수의 합을 뺀다.
print("덧셈 뺄셈 합계 (2/4)")
while 1:
    n = int(input("n : "))
    if n == 0:      # 입력값이 0이면 종료
        break
    odd = 0
    even = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even += i
        else:
            odd += i
    sum = odd - even
    print(f'홀수합 : {odd}')
    print(f'짝수합 : {even}')
    print(f'합계 : {odd}-{even} = {sum}')
