"""
실습 12 풀이: 복합 조건식
"""

score = int(input("점수 입력: "))
attendance = int(input("출석률 입력: "))

# 점수가 80 이상이고 출석률이 90 초과이면 수료 가능
if score >= 80 and attendance > 90:
    print("수료 가능")
else:
    print("수료 불가")
