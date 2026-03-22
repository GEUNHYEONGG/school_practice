"""
실습 1 풀이: 간단한 계산기
"""

# input()은 문자열을 반환하므로 int()로 정수 변환
a = int(input("첫 번째 수: "))
b = int(input("두 번째 수: "))

# 7가지 산술 연산자로 결과 출력
# print()에 쉼표(,)로 값을 나열하면 공백으로 구분되어 출력된다
print("더하기:", a + b)
print("빼기:", a - b)
print("곱하기:", a * b)
print("나누기:", a / b)  # / 나누기는 항상 소수점(float) 결과
print("몫:", a // b)
print("나머지:", a % b)
print("거듭제곱:", a ** b)
