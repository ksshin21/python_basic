# 40일차 바둑알 합계 - 1차 시도 (KS)
# 바둑알이 한 줄씩 늘어날 때 n번째 삼각형까지의 모든 바둑알의 개수
#                        O
#                  O    OO
#            O    OO   OOO
#       O   OO   OOO  OOOO
#  O   OO  OOO  OOOO OOOOO  ......
#
print("바둑알 개수 구하기")
while 1:
    n = int(input("n : "))
    if n == 0:      # 0을 입력받으면 메시지 출력하고 종료
        print('Program terminated!')
        break
    sum = 0                     # 바둑알의 합계를 저장할 변수
    for i in range(1, n+1):     # n번째 삼각형까지 반복
        for j in range(1, i+1): # 1부터 i까지 개수의 합을 구함
            sum += j
    print(f'{sum}')
