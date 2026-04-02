"""
실습 21 풀이: 로그인 확인
"""

is_logged_in = input("로그인 여부 (y/n): ")

# not: 조건을 반대로 뒤집는다
# is_logged_in == "y"가 아니면 → 로그인 상태가 아님
if not is_logged_in == "y":
    print("로그인이 필요합니다")


