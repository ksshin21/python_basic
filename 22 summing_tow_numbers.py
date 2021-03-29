# 22일차 암산왕1 - 1차시도 (KS)
print('암산왕 v0.1')
ans = 0   # 정답의 수 
cnt = 0   # 총 문제 수
while True:
    a = int(input('정수 : '))
    b = int(input('정수 : '))
    if a == 0 and b == 0:
        # 정답의 개수를 전체 문제의 수로 나눈 후 100을 곱해서 성적을 구함
        score = int(round(ans/cnt * 100))
        print('[정답수 {}개, 문제수 {}개, 암산성적 {}점]'.format(ans, cnt, score))  
        break
    print('{} + {} = '.format(a, b), end='')
    sumIn = int(input())
    res = a + b
    if sumIn == res:
        print('정답!')
        ans += 1    # 성적을 구하기 위해 정답의 개수를 구함
    else:
        print('틀림! 정답: ', res)
    cnt += 1
