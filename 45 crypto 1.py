#45일차 암호미션1(아스키코드) - 1차 시도 (KS)
# 문자 하나를 입력받아 그 문자부터 시작하여 아스키코드 순으로 26개의 문자를 이어서 출력하라.
# 문자하나에서 엔터를 치면 프로그램 종료
# 입력받은 문자에 저장된 변수가 c라면 문자를 아스키코드로 바꾸는 함수는 ord(c)
ch_no = 26      # 출력할 문자 개수를 변경하려면 이 값을 바꾼다.
while 1:
    c = input("문자하나 : ")
    if c == '':      # 입력받은 문자하나가 엔터이면 종료. Enter를 입력하면 input 함수의 반환값은 빈칸이 됨
        break
    for i in range(ch_no):
        ascii_c = ord(c)
        print('%c'%(ascii_c), end='')
        ascii_c += 1
        c = chr(ascii_c)
    print('')
