# 10일차
#별찍기-이등변삼각형 1차시도(KS)
while True:
    n = int(input('줄 수 : '))
    if n == 0:
        break
    for i in range(1,n+1):
        num = i * 2 - 1
        line = n * 2 + 1
        print(('*'*num).center(line))
