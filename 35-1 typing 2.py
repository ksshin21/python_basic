# 35일차 타자 측정기 v0.2 - 2차 시도 (KS)
# 문장 : text = ['Now is better than never.',
#               'Life is too short, you need python.',
#               'Happy python']
import time
print('타자측정기 v0.2')
text=['Now is better than never.',
      'Life is too short, you need python.',
      'Happy python!']
sumLength=0 # 글자 길이 합계
sumCho=0    # 걸린 초 합계
for sentence  in text: # text 에서 한 문장씩 꺼내기
    length=len(sentence) # 한 문장의 글자수
    while 1:
        print(">"+sentence) # 타자 칠 내용
        start=time.time()
        inStr=input('>')    # 타자 입력 문자열
        if sentence==inStr:break # 맞으면 입력 종료
        print('오타가 있습니다.')  # 아니면 반복
    end=time.time()
    cho=end-start
    taBun=length/cho*60
    print(f'{taBun:.0f}타/분')
    sumLength+=length # 글자수 누적
    sumCho+=cho       # 걸린시간 초 누적
sumtaBun=sumLength/sumCho*60  # 전체 타수/분
print(f'전체 {sumtaBun:.0f}타/분')
