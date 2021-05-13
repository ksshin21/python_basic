# 36일차 정렬하기2 - 선택정렬 - 1차 시도 (KS)
# 주어진 리스트를 선택 정렬을 사용하여  점수를 오름차순으로 정렬
# pList=[95,73,82,83,64,89,77,48,74,99]
# sort(), zip() 사용
print('정수 선택정렬 오름차순')
nameList=['김','이','박','최','정','강','조','윤','장','임']
pList=[95,73,82,83,64,89,77,48,74,99]
dic = { name : value for name, value in zip(nameList, pList) }
for name, value in sorted(dic.items()):
    print(name, value)
