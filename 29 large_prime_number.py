# 29일차 소수판정 v0.2 큰 수 시간단축 - 2차 시도 (KS)
# 루트n까지 검사
import time as t
print('소수판정 v0.2 (큰 수)')
def isPrime(n):  # 소수인지 판정하는 함수
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while 1:  # 함수호출 소수판정
    n = int(input('예 9147483647 정수입력 : '))  # 정수 입력
    if n == 0: break
    startTime = t.time()
    if isPrime(n):
        print('소수')
    else:
        print('소수 아님')
    endTime = t.time()
    eTime = endTime - startTime
    print('걸린시간 : %.3f초'%eTime)
