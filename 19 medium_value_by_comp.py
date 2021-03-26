# 19일차 중앙값 구하기 - 1차시도 (KS)
while True:
    a, b, c = map(int, input('정수 3개 띄어쓰기로 입력 (끝내려면 모두 0 입력) : ').split())
    if a == b == c == 0:
        break

    if a >= b:
        if b >= c:
            m = b      # a >= b >= c
        elif a >= c:    # a >= b, b < c 인 경우
            m = c      # a >= c > b
        else:            # a >= b, b < c, a < c 인 경우
            m = a     # c > a >= b
    elif c >= b:      # a < b 인 경우
        m = b         # c >= b > a
    elif c >=a:       # a < b, c < b 인 경우
        m = c         # b > c >= a
    else:               # a < b, c < b, c < a 인 경우
        m = a        # c < a < c
    print('중앙값 = ', m)
