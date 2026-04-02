"""
실습 22 풀이: 이벤트 참여 판정
"""

is_member = input("회원 여부 (y/n): ")
age = int(input("나이를 입력하세요: "))
is_vip = input("VIP 여부 (y/n): ")

# 조건 분석:
# 1) 회원이어야 한다 → is_member == "y"
# 2) 나이가 20세 이상이거나 VIP → (age >= 20 or is_vip == "y")
# 두 조건을 and로 연결: 1) 그리고 2) 모두 만족해야 함
# 괄호로 or 조건을 묶어야 and보다 먼저 평가된다
can_join = is_member == "y" and (age >= 20 or is_vip == "y")

if can_join:
    print("이벤트 참여 가능")
else:
    print("이벤트 참여 불가")
