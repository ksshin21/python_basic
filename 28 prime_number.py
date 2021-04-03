# 28일차 소수판정 v0.1 - 2차 시도 (KS)
print('소수판정 v0.1 : 정수를 입력받아 소수인지 판정하는 함수 만들기')
def isPrime(n): # 소수인지 판정하는 함수
    # 1과 자기 자신만으로 나누어져야 소수이므로 그 밖의 수로 나누어지면 소수가 아님
    # 단, 2%2는 0이지만 2는 소수이므로 별도로 처리해 줌
    if n == 1: return False    # 1은 소수가 아님
    if n == 2: return True     # 2는 소수
    for i in range(2, n):
        if n % i == 0:
            print('나눠지는 수 = %d'%i)
            return False
    return True

while 1:    # 함수호출 소수판정
    n = int(input('정수 입력 : '))    # 정수 입력
    if n == 0:  break
    if isPrime(n):
        print('소수')
    else:
        print('소수 아님')
