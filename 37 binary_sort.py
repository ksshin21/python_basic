# 37일차 정렬하기2 - 선택정렬 - 1차 시도 (KS)
# 주어진 리스트를 선택 정렬을 사용하여  점수를 오름차순으로 정렬
# pList=[95,73,82,83,64,89,77,48,74,99]
# sort(), zip() 사용
print('정수 선택정렬 오름차순')
pList=[95,73,82,83,64,89,77,48,74,99]
n = len(pList)
print('정렬 과정')
for i in range(n-1):
    least = i
    for j in range(i+1, n):
        if pList[least] > pList[j]:
            least = j
    pList[i], pList[least] = pList[least], pList[i]
    print(f'{i}차 {pList}')