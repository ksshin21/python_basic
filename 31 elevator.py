# 31일차 엘리베이터 등가속 운동 - 1차 시도 (KS)
# 처음 속도가 가장 늦고 맨마지막 층간 속도가 가장 빠르다.
# 입력 : 엘리베이터 층 수
import time as t
while 1:
    n = int(input('가고 싶은 층 수를 입력 : '))    # 엘리베이터로 올라가려는 층 수 입력
    if n == 0: break
    for i in range(n+1):
        interval = 1 - i/n
        print('%d층 interval : %.2f초'%(i,interval))
        t.sleep(interval)
    print('도착')
