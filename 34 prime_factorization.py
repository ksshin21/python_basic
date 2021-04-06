# 34일차 소인수 분해 v0.2 - 1차 시도 (KS)
# 반복하여 정수를 입력받아 소인수분해
# 거듭제곱은 caret(^) 이용하여 표현
# 1은 출력하지 않고 0이 입력되면 프로그램 종료
print('소인수분해 v0.2')
while 1:
    n = int(input('정수 : '))  # 정수 입력
    if n == 0: break
    res = ""
    for i in range(2, n+1):
        count = 0
        while n % i == 0:
            count += 1
            n = n // i      # 정수 나누기, 결과를 정수로
        if count >= 2:
            res += f'{i} ^ {count} x '
        elif count == 1:
            res += f'{i} x '
    print(res[:-3])
