"""
실습 15 풀이: 회원 할인 (삼항 연산자)
"""

price = int(input("가격 입력: "))
is_member = int(input("회원 여부 (1: 회원, 0: 비회원): "))

# 회원이면 20% 할인, 비회원이면 5% 할인
discount = 0.2 if is_member else 0.05
final_price = int(price * (1 - discount))
print(f"최종 가격: {final_price}원")
