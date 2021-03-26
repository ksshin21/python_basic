# 17일차 숫자찍기-왼쪽직각삼각형  1차시도 (KS)
while True:
    n = int(input('층 수 : '))
    if n == 0:
        break
    k = 0
    for i in range(1, n+1):
        for j in range(i):
            k += 1
            print(k % 10, end='')
        print('')
