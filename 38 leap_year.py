# 38일차 윤년 알고리즘 - 1차 시도 (KS)
print("윤년 알고리즘")
while 1:
    year = int(input("연도 : "))
    if year == 0: break
    if ( (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 ):
        print("윤년")
    else:
     print("평년")
