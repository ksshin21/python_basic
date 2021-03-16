# 1일차 정수를 입력받아 홀수 짝수 구분하기
while True:
    a = input("정수입력(press q to stop) : ")
    if (a == 'q') :
        break
    else :
        num = int(a)
        if (num % 2) == 1:
            print("홀수")
        else : 
            print("짝수")
