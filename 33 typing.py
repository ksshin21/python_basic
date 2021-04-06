# 33일차 타자 측정기 v0.1 - 1차 시도 (KS)
# 문장 : text = 'Explicit is better than implicit.'
import time as t
print('타자측정기 v0.1')
text = 'Explicit is better than implicit.'
length = len(text)
while 1:
    print('>'+text)     # 타자할 텍스트 출력
    startTime = t.time()
    str = input('>')    # 타자 내용 입력
    if str == text:
        break
    print('오타가 있습니다.')
endTime = t.time()
res = length/(endTime - startTime) * 60    # 초 단위의 시간을 분으로 환산
print('%.0f타/분'%(res))      # 소수 첫째 자리에서 반올림
