# 15일차 
#숫자찍기-n*n - 1차시도(KS)
while True:
    n = int(input('층수 n : '))
    if n == 0:
        break;
    for i in range(1, n+1):
        for j in range(1, n+1):
            print((j + n * (i-1)) % 10, end='')
        print('')
