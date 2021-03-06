# 39일차 전기요금 계산 - 1차 시도 (KS)
print("전기 요금 계산")
while 1:
    n = int(input("사용량(kw) : "))
    if n == 0:      # 0을 입력받으면 메시지 출력하고 종료
        print('Are you alive?')
        break
    if n <= 50:     # 1~50kWh 까지는 30원으로 계산
        rate = n * 30
    elif n <= 100:  # 51~100kWh 까지는 1~50까지 30원, 51보다 큰 수에 대해 80원으로 계산
        rate = 50 * 30 + (n-50) * 80    # 예) 53이면 50*30+3*80
    else:           # 100kWh 를 초과하는 값에 대해서는, 1~50까지 30원, 51~100까지 80원, 101부터 120원으로 계산
        rate = 50 * 30 + 50 * 80 + (n-100) * 120       # 두번째 50은 100-50의 값, 예) 105이면 50*30+(100-50)*80+5
    print(f'{rate} 원')
