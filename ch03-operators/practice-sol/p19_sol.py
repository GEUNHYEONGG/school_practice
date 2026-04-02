"""
실습 19 풀이: 수료 판정
"""

score = int(input("점수를 입력하세요: "))
attendance = int(input("출석률을 입력하세요: "))

print("점수:", score)
print("출석률:", attendance)

# 두 조건을 and로 조합: 둘 다 만족해야 True
is_pass = score >= 80 and attendance > 90

# True이면 "수료 가능", False이면 "수료 불가" 출력
if is_pass:
    print("수료 가능")
else:
    print("수료 불가")
