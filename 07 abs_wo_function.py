#알고리즘 7일차 절댓값 1차시도 (KS)
# abs() 함수 이용하지 않고 절대값 구하기
while True:
    n = int(input('정수 입력: '))
    if n == 0:
        break;   
    if n < 0:
        n = -n
    print('절댓값: ', n)
