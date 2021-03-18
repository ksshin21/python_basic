# 2일차
# 두 정수값을 입력 받아 a, b에 저장 (KS)
a = int(input("정수 입력 : a = "))
b = int(input("정수 입력 : b = "))

# 두 정수 a, b의 값 출력
print("*** a, b의 값 ***")
print(a,b)

# 두 변수의 값 교환
a, b = b, a

# 치환된 두 정수 a, b의 값 출력
print("*** 값 교환 후 a, b의 값 ***")
print(a, b)
