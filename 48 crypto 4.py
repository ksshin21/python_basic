#48일차 암호미션4(아스키코드 암호생성) - 1차 시도 (KS)
# 영어로 3줄로 작성된 msg.txt 파일을  읽어 암호를 생성하여 출력하는 프로그램
# msg.txt 파일은 자신이 원하는 문장
with open('msg.txt') as f:
    lines = f.readlines()
print('[Contents : msg.txt]')
for i in range(len(lines)):     # msg.txt 파일의 내용을 먼저 보여준다.
    print(lines[i], end='')
print('\n')
for i in range(len(lines)):
    print('[ ', end='')
    for j in range(len(lines[i])):
        ch = lines[i][j]        # 파일에서 읽어들인 내용에서 한 문자씩 암호화하기 위해 변수에 저장한다.
        print(ord(ch)-ord('a')+1, end=' ')  # 알파벳 a를 1의 값으로 기준 삼아 각 문자를 암호화한다.
    print(']')
