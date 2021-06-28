#49일차 암호미션5(카이사르 암호생성) - 1차 시도 (KS)
# 카이사르 암호는 알파벳 대문자 1:1 대응을 하여 만들어지는 암호이다.
# key가 3이면 ABC부터 차례로 3칸을 오른쪽으로 밀어 쓰게 되므로 DEF 가 나오고 XYZ이라면 ABC가 나오게 된다.
# 알파벳 대문자 외에는 모두 입력한 문자가 그대로 나오게 하면 된다.
# 1.알파벳 대문자 26자를 아스키코드를 이용해서 출력한다.
# 2.알파벳 대문자가 있는 문장 출력
# 3.암호화 키 입력
# 4.카이사르 암호화 된 문장 출력
#
msg = 'XYZ COME TO ROME!'
print('암호미션5(카이사르 암호생성)')
alpha = ''
for c in range(ord('A'), ord('Z')+1): # A부터 Z까지 알파벳 대문자 문자열 생성
    alpha += chr(c)
print(alpha)            # 알파벳 대문자 출력
alpha = alpha * 2       # Z를 넘어가는 알파벳을 위해 여유있는 영역을 만들어줌
print(msg)              # 알파벳 대문자가 있는 문장 출력
key = int(input('key: ')) # 암호화 키 입력
for c in msg:           # 주어진 문장에서 한 글자씩 선택
    if 'A' <= c <= 'Z': # 대문자이면
        code = ord(c) - ord('A') + key
        print(alpha[code], end='')
    else:
        print(c, end='')
print('')