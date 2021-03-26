# 18일차 약수구하기 - 1차시도 (KS)
while True:
    n = int(input('정수 : '))
    if n == 0:
        break
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=',')
    print('')
