#50일차 소수출현확률 1차시도 (KS)
import time as t
print('소수출현비율 v0.1 (KS)')

# 소수를 구하는 함수
def prime_list(n):
    sieve = [True] * n      # 인자로 받은 n개만큼(0부터 n-1까지) 배열을 True로 초기화
    sieve[0] = sieve[1] = False     # 0번째와 1번째 배열원소는 False
    m = int(n ** 0.5)           # 제곱근을 구함
    for i in range(2, m+1):     # 2부터 제곱근까지 배수에 대해 False 값을 넣을 것임
        if sieve[i] == True:    # True 값을 갖는 것 중에서(초기값은 모두 True)
            for j in range(i+i, n, i):  # 2부터 시작하여 자신의 배수에 대해 False 값을 넣음
                sieve[j] = False
    return sieve

while 1:
    n = int(input('소수범위(100의 배수): '))   # 100의 배수 정수를 입력받음
    if n == 0: break    # 0을 입력하면 프로그램을 종료

    # 변수 초기화
    step = n//10    # 입력받은 숫자를 10구간 단위로 나누기 위함
    start = 0       # 10구간 단위의 시작 인덱스
    end = step      # 10구간 단위의 끝 인덱스
    cnt = [0]*10    # 10구간 단위마다 소수의 개수를 세기 위한 배열
    total_cnt = 0   # 소수의 총 개수를 저장하는 변수
    idx = 0         # 인덱스 변수

    startTime = t.time()        # 경과 시간 재기 : 시작 시간
    sieve = prime_list(n)       # 입력 받은 숫자까지의 소수를 모두 구하여 리스트로 리턴
    while end <= n:             # 10구간 단위로 n까지 소수 개수 계산
        for i in range(start, end):  # 10구간 단위로 시작 위치와 끝 위치가 바뀜
            if sieve[i]:        # 함수에서 구한 리스트에 참값이 있으면 소수이므로 카운트
                cnt[idx] += 1
        total_cnt += cnt[idx]   # 각 구간의 개수를 총 개수에 더함
        start += step           # 10구간을 한 구간씩 옮겨줌, 시작 위치
        end += step             # 10구간을 한 구간씩 옮겨줌, 끝 위치
        idx += 1                # 10구간의 개수 리스트의 인덱스를 하나 증가
    endTime = t.time()          # 경과 시간 재기 : 끝 시간
    eTime = endTime - startTime     # 경과 시간

    # 10구간 단위의 소수 개수 출력을 위한 변수 초기화
    start = 0
    end = step = n // 10
    idx = 0

    # 10구간 단위의 소수 개수 및 구간 내에서의 개수 비율 출력
    while end <= n:
        print('%8d ~ %8d %6d개 %.2f%%' % (start, end, cnt[idx], cnt[idx]/step*100))
        start += step
        end += step
        idx += 1

    # 경과 시간 출력
    print('\n%d개, 걸린시간 : %.3f초'%(total_cnt, eTime))
