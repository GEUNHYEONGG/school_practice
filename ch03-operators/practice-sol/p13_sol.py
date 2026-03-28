"""
실습 13 풀이: 합격 여부 (삼항 연산자)
"""

score = int(input("점수 입력: "))

# 삼항 연산자: 참일 때 값 if 조건 else 거짓일 때 값
result = "합격" if score >= 70 else "불합격"
print(result)
