# 19일차 중앙값 구하기 - 2차시도 (KS)
# 입력받은 정수를 오름차순으로 만들어 중앙값을 구함
while True:
    a, b, c = map(int, input('정수 3개 띄어쓰기로 입력 (끝내려면 모두 0 입력) : ').split())
    if a == b == c == 0:
        break

    if a > b: a, b = b, a   # a,b 중 큰 수를 뒤로
    if a > c: a, c = c, a   # a,c 중 큰 수를 뒤로
    if b > c: b, c = c, a   # b,c 중 큰 수를 뒤로
    print('중앙값 = ', b)
