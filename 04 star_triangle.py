# 4일차 
#별찍기-직각삼각형 1차시도 (KS)
while True:
    n = int(input("별의 개수 : "))
    if n == 0:
        break
    for i in range(n):
        print('*'*(i+1), end='')
        print()
