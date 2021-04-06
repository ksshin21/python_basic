# 35일차 타자 측정기 v0.2 - 1차 시도 (KS)
# 문장 : text = ['Now is better than never.',
#               'Life is too short, you need python.',
#               'Happy python']
import time as t

print('타자측정기 v0.2')
text = ['Now is better than never.',
        'Life is too short, you need python.',
        'Happy python']
length = len(text)  # text 리스트에 있는 원소의 개수

ll = []  # text 리스트 각 항목의 길이를 넣는 리스트
for i in range(length):  # text 리스트 각 항목의 길이를 ll 리스트에 넣어줌
    ll.append(len(text[i]))

i = 0
eTime = []  # 각 텍스트 입력하는데 걸리는 시간을 저장할 리스트
while i < length:  # text 리스트에 있는 항목의 개수만큼 처리
    print('>'+text[i])     # 타자할 텍스트 출력
    startTime = t.time()
    str = input('>')    # 타자 내용 입력
    if str != text[i]:
        print('오타가 있습니다.')
    else:
        endTime = t.time()
        eTime.append((endTime - startTime))  # 입력한 문자열과 text 리스트에 있는 문자열이 같으면 시간 측정
        res = ll[i]/(eTime[i]) * 60    # 초 단위의 시간을 분으로 환산
        print('%.0f타/분'%(res))      # 소수 첫째 자리에서 반올림
        i += 1  # 오타가 아니면 인덱스를 증가, 오타이면 다시 typing하도록 인덱스를 증가시키지 않음
list_sum = sum(ll)/sum(eTime) * 60   # 전체글자수(누적글자수)를 각 문자열별로 걸린 시간의 합(누적초)으로 나눈 시간 * 60
print('전체 %.0f타/분'%(list_sum))