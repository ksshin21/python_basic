# 13일차
#합계 시간재기 - 최선의 방법 1차시도(KS)
import  time as t
startTime=t.time()  # 시작시간
s=0
start=10000000      # 천만
end=20000000
for i in range(start,end+1):
    s += i
endTime=t.time()
eTime=endTime-startTime # 경과시간(걸린 시간)
print(s)
print('경과시간:%.3f초'%eTime)
