'''
2914 - 저작권
첫째 줄에서 앨범에 수록된 곡의 개수 A와 평균값 I를 입력받고, 저작권이 있는 멜로디의 최소 갯수를 출력해야 하는 문제

예를 들어서 평균값 I가 24로 주어졌을 때, 이 값은 올림을 하여 나온 값이므로 실제 평균값은 23<I<=24 범위 내의 값임을 알 수 있다.
'적어도'의 경우를 구해야 하므로 I에서 1을 뺀 값에 A를 곱하는 역연산을 해준다.
그러나 이는 평균이 23일 때의 경우이므로, 마지막에 1을 더해주면 최소 갯수가 된다.
'''

import sys

a, i = map(int, sys.stdin.readline().split())
print(a * (i - 1) + 1)
