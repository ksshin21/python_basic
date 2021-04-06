# 35일차 타자 측정기 v0.2 - 2차 시도 (KS)
# 문장 : text = ['Now is better than never.',
#               'Life is too short, you need python.',
#               'Happy python']
import time as t
print('타자측정기 v0.2')
text=['Now is better than never.',
      'Life is too short, you need python.',
      'Happy python!']
sumLength = 0 # 글자 길이 합계
sumSec = 0    # 걸린 초 합계
for sentence in text: # text 에서 한 문장씩 꺼내기
    length = len(sentence) # 한 문장의 글자수
    while 1:
        print(">" + sentence) # 타자 칠 내용
        start = t.time()
        inStr = input('>')    # 타자 입력 문자열
        if sentence == inStr:
            break               # 맞으면 입력 종료
        print('오타가 있습니다.')  # 아니면 반복
    end = t.time()
    sec = end-start
    typeMin = length / sec * 60
    print(f'{typeMin:.0f}타/분')
    sumLength += length # 글자수 누적
    sumSec += sec       # 걸린시간 초 누적
sumMin = sumLength/sumSec*60  # 전체 타수/분
print(f'전체 {sumMin:.0f}타/분')
