"""
실습 20 풀이: 입장 판정
"""

age = int(input("나이를 입력하세요: "))
guardian = input("보호자 동반 여부 (y/n): ")

print("나이:", age)
print("보호자 동반:", guardian)

# guardian == "y"는 문자열 비교 → True 또는 False
# or: 둘 중 하나라도 True이면 입장 가능
is_allowed = age >= 20 or guardian == "y"

# if/else: 조건에 따라 다른 내용을 출력
if is_allowed:
    print("입장 가능")
else:
    print("입장 불가")
