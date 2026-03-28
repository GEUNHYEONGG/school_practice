"""
실습 14 풀이: 홀짝 판별 (삼항 연산자)
"""

num = int(input("정수 입력: "))

# 2로 나눈 나머지가 0이면 짝수
result = "짝수" if num % 2 == 0 else "홀수"
print(result)
