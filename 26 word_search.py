# 26일차 영어단어 검색 v0.1 - 1차시도 (KS)
myDic = { 'sky':'하늘', 'apple':'사과', 'can':'깡통', 'boat':'배',
          'sea':'바다', 'smile':'미소', 'animal':'동물', 'park':'공원' }
print('영어 단어 검색 v0.1')
while 1:
    word = input('단어 입력 : ')
    if not word:
        break
    print(word, myDic.get(word, '없음'))
