# 24일차 큰수 약수 구하기 v0.1 - 1차시도 (KS)
import time as t
startTime = t.time()    # 시작 시간
n = 100000000    # 1억
cnt = 0
for i in range(1, n+1):
    if n % i == 0:    # n이 i로 나누어 떨어지면
        print(i, end=',')
        cnt += 1
endTime = t.time()    # 끝 시간
eTime = endTime - startTime    # 경과시간
print(' {}개,'.format(cnt),'걸린시간:%.3f초'%eTime)
