# 12일차 
#시간재기 - for 반복문 1차시도(KS)
import  time as t
startTime=t.time() #시작시간
for i in range (10000000): #천만 
    pass
endTime=t.time()
eTime=endTime-startTime # 경과시간(걸린 시간)
print('경과시간:%.3f초'%eTime)
