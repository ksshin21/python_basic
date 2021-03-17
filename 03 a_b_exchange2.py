# 3일차
#치환 1차 시도

a = int(input("a 입력: "))
b = int(input("b 입력: "))
print(f'a={a} b={b}')

# temp를 이용하여 a, b 값 치환
temp = a
a = b
b = temp

print("두 변수의 값 치환")
print(f'a={a} b={b}')
