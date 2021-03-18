# 8일차 
# 별찍기 - 오른쪽직각삼각형 1차시도 (KS)
while True:
    n = int(input('별의 개수: '))
    if n == 0:
        print('***** Bye~! *****')
        break;
    for i in range(n):
        print(' '*(n-i+1), '*'*(i+1), end='')
        print('')
        
