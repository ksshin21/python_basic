# 25일차 큰수 약수 구하기 v0.2 - 2차시도: 시간재기 구간에서 입출력을 제외하기  (KS)
import time as t
while 1:
    cnt = 0
    n = int(input('1조이하 정수 : '))
    if n == 0:
        break
    m = int(n ** 0.5)    # n의 제곱근
    nList = []    # 나눗셈의 몫을 큰 값부터 제곱근까지 저장
    resList = ''

    startTime = t.time()    # 시작 시간
    for i in range(1, m+1):
        if n % i == 0:    # n이 i로 나누어 떨어지면
            #print(i, end=',')    # 작은 약수부터 출력
            resList += f'{i},'
            nList.append(n // i)    # 몫 중 큰 값부터 리스트에 추가
            cnt += 1
    end = len(nList) - 1    # 마지막 값이 들어간 위치
    if i == nList[end]:    # 작은 값 쪽의 약수와 큰 값쪽의 약수가 같으면
        end -= 1

    for i in range(end, -1, -1):    # 큰 값들의 리스트를 거꾸로 출력
        #print(nList[i], end=',')
        resList += f'{nList[i]},'
        cnt += 1
    endTime = t.time()    # 끝 시간
    print(resList)
    eTime = endTime - startTime    # 경과시간
    print('%d개, 걸린시간:%.3f초'%(cnt, eTime))
