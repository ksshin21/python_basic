# 6일차
# 별찍기 - 역직각삼각형 1차시도 (KS)
while True:
    n = int(input('별의 개수: '))
    if n == 0:
        print("***** Bye~! *****")
        break
    while n > 0:
        print('*'*n, end='')
        print('')
        n -= 1
