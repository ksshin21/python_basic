# 11일차 
#합계구하기 - for 반복문 1차시도(KS)
# 이 프로그램은 음수를 포함한 두 정수 범위(양 끝 수 포함)의 합계를 구합니다.
# 프로그램을 종료하기 위해서는 문자 'q'를 입력하세요.
while True:
    print('\nIf you want to stop, press q ...')
    start = input('시작 수(음수 포함 정수) : ')
    if start == 'q':        # 음수도 처리하기 위해 마침 문자를 따로 지정
        break
    first = int(start)      # first = int(first)로 작성해도 가능
    last = int(input('끝 수(음수 포함 정수) : '))

    sum = 0
    for i in range(first, last+1):
        sum += i
    print('합계 : ', sum)
