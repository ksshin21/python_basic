# 20일차 리스트 검색1 - 1차시도 (KS)
wordList = ['cat', 'dog', 'pig', 'hen', 'cow', 'duck', 'cat']
while True:
    s = input('단어입력 : ')
    if s == '':
        break
    for i in range(len(wordList)):
        if s == wordList[i]:
            print('{}는 {}번째에 있다.'.format(s, i+1))
