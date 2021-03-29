# 23일차 리스트 검색3 - 1차시도 (KS)
wordList = ['cat', 'dog', 'pig', 'hen', 'cow', 'duck', 'cat']
print('리스트 단어검색 v0.3')
while True:
    s = input('단어입력 : ')
    if s == '':
        break
    n = 0
    for i in range(len(wordList)):
        if s == wordList[i]:
            n = n + 1
            print('{}는 {}번째에 있다.'.format(s, i+1))
    if n == 0:
        print('{}는 없음 '.format(s), end='')
        yes_no = input(' 추가할까요?(y/n): ')
        if yes_no == 'y':
            wordList.append(s)
            print('추가되었습니다.')
