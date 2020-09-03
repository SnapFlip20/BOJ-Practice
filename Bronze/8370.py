'''
8370 - Plane
바이트랜드 항공사에서 새로운 비행기 모델을 만들었는데
좌석의 배치가 비즈니스 클래스에는 1열 당 k1개씩 n1열, 이코노미 클래스에는 1열 당 k2개씩 n2열이라고 할 때,
한 줄에 n1, k1, n2, k2 값을 순서대로 입력받고 모든 좌석의 개수를 출력해야 하는 문제

(n1*k1 + n2*k2)를 계산해서 출력하면 된다.
'''

import sys

n1, k1, n2, k2 = map(int, sys.stdin.readline().split())

print(n1*k1 + n2*k2)
