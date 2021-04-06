# 30일차 소수판정 v0.3 큰수범위 소수개수 - 1차 시도 (KS)
# 1부터 100만까지 사이의 숫자 중 소수의 개수를 구함
# 입력 : 소수범위 시작 : 1
#       소수범위 끝 : 1000000
# 출력 : _개 걸린시간 : _초
import time as t

def isPrime(n):  # 소수인지 판정하는 함수
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while 1:  # 함수호출 소수판정
    print('소수판정 v0.3 큰 수 범위 소수 개수')
    cnt = 0     # 소수 개수를 저장하는 변수
    m = int(input('소수범위 시작 : '))  # 소수범위 시작 숫자 입력
    n = int(input('소수범위 끝 : '))    # 소수범위 끝 숫자 입력
    if m == 0 or n == 0: break

    startTime = t.time()
    for i in range(m, n+1): # 시작값부터 끝값까지 숫자 하나하나 소수인지를 검사
        if isPrime(i):      # 각 숫자가 소수이면 cnt를 하나씩 증가시킴
            cnt += 1
    endTime = t.time()
    eTime = endTime - startTime
    print('%d개 걸린시간 : %.3f초'%(cnt, eTime))
