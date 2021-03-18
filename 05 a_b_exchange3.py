# 5일차
# 치환 - 덧셈뺄셈사용 1차시도(KS)
a = int(input('a 입력:'))
b = int(input('b 입력:'))
print(f'a={a} b={b}')
print('두 변수의 값 치환')
a = a + b
b = a - b
a = a - b
print(f'a={a} b={b}')
