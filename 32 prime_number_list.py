# 32일차 소인수 분해 v0.1 - 1차 시도 (KS)
# 반복하여 정수를 입력받아 소인수분해
# 1은 출력하지 않고 0이 입력되면 프로그램 종료
# 입력 : 정수 : 12
# 출력 : 2 x 2 x 3 x

# 소수인지 판정하는 함수
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2부터 입력받은 수(n)까지 모든 소수를 구해서 list로 리턴하는 함수
def prime_numbers_list(n):
    int_list = (x for x in range(2, n+1))
    prime_numbers = []
    for i in int_list:
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

# main routine
print('소인수분해 v0.1')
while 1:
    n = int(input('정수 : '))  # 정수 입력
    if n == 0: break
    if n == 1: continue

    primes = prime_numbers_list(n)    # 입력 정수 n의 소인수들의 리스트 만들기
    for p in primes:
        count = 0       # 같은 소수로 몇 번 나누어지는가를 세기 위한 변수
        while n % p == 0:
            count += 1
            n = n // p
        while count > 0:    # 시간을 잴 필요가 없으므로 바로 출력함
            print('%d'%(p), end=' x ')
            count -= 1
    print('')
