#47일차 암호미션3(아스키코드) - 2차 시도 (KS)
# 리스트의 암호문을 해독하는 프로그램을 작성하라
# code=[ [1, -64, 2, 15, 15, 11],
#        [-24, 5, 12, 12, 15, -64, 23, 15, 18, 12, 4, -63],
#        [-7, 15, 21, -64, 14, 5, 5, 4, -64, 16, 25, 20, 8, 15, 14, -50] ]
code=[ [1, -64, 2, 15, 15, 11],
       [-24, 5, 12, 12, 15, -64, 23, 15, 18, 12, 4, -63],
       [-7, 15, 21, -64, 14, 5, 5, 4, -64, 16, 25, 20, 8, 15, 14, -50] ]
print('암호해독 : 이 문제는 정말 암호다!!!')
row = len(code)         # 2차원 리스트이므로 row의 개수. 실행시간을 줄이기 위해 미리 구한다.
for i in range(row):    # row의 개수만큼 반복
    column = len(code[i])       # column의 개수. 실행시간을 줄이기 위해 미리 구한다.
    for j in range(column):     # column의 개수만큼 반복
        num = code[i][j] + ord('a') - 1  # 문자 a의 ascii code를 이용, 1을 a라 생각해서 만든 코드
        ch = chr(num)
        print(f'{ch}', end=' ')
    print('')
