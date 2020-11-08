'''
6768 - Don't pass me the ball!
번호가 1번에서 99번까지 부여된 축구선수들이 있다
골을 넣기 전에 공을 터치한 선수 세 명의 번호가 증가하는 순이어야 골이 인정된다고 한다
마지막으로 공을 터치한 선수의 번호 J가 주어졌을 때,
앞의 세 선수로 가능한 조합의 수를 출력해야 하는 문제

J가 1, 2일 경우에는 가능한 조합의 수가 없으므로 0을 출력하고,
J가 3~99일 경우에는 JC3의 결과를 출력한다.
'''

import sys

n = int(sys.stdin.readline())

if n < 3:
    print(0)
else:
    print(((n-1)*(n-2)*(n-3))//6)
