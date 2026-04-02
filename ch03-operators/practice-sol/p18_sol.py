"""
실습 18 풀이: 조건식 작성 연습
"""

# ========================================
# [1단계] 성적 관련
# ========================================
score = 85
attendance = 92

print(score >= 80)                                  # True
print(score > 90)                                   # False
print(attendance <= 95)                              # True
print(attendance < 80)                               # False
print(score == 100)                                  # False
print(score >= 80 and attendance >= 90)              # True
print(score >= 90 or attendance >= 95)               # False
print(score >= 70 and attendance >= 80)              # True

# ========================================
# [2단계] 입장 관련
# ========================================
age = 17
guardian = True
height = 168
weight = 60

print(age >= 20)                                     # False
print(age < 19)                                      # True
print(height >= 170)                                 # False
print(weight <= 65)                                  # True
print(age == 17)                                     # True
print(height == 168)                                 # True
print(guardian)                                      # True
print(not guardian)                                  # False
print(age >= 20 or guardian)                         # True
print(height >= 170 and weight <= 65)                # False
print(guardian and age < 19)                         # True
print(height >= 165 or weight <= 55)                 # True

# ========================================
# [3단계] 회원 관련
# ========================================
is_vip = False
is_member = True
money = 12000

print(is_vip)                                        # False
print(is_member)                                     # True
print(not is_vip)                                    # True
print(not is_member)                                 # False
print(money >= 10000)                                # True
print(money < 5000)                                  # False
print(money == 12000)                                # True
print(is_vip or is_member)                           # True
print(money >= 10000 and is_member)                  # True
print(not is_vip and is_member)                      # True
print(not is_member and guardian)                     # False

# ========================================
# [4단계] 종합
# ========================================
temperature = 28

print(temperature > 30)                              # False
print(temperature >= 25)                             # True
print(temperature == 28)                             # True
print(weight != 60)                                  # False
print(score < 60 or attendance < 70)                 # False
print(attendance >= 90 and not is_member)             # False
print(money >= 10000 and not guardian)                # False
print(not guardian and age >= 20)                     # False
print(score >= 80 and not is_vip)                    # True
print(score >= 70 or not is_vip)                     # True
print(not is_member or age >= 20)                    # False
print(money < 5000 or temperature > 30)              # False

# 괄호가 필요한 복합 조건
# and가 or보다 먼저 계산되므로, or 조건을 괄호로 묶어야 의도대로 동작
print(score >= 80 and (attendance >= 90 or is_vip))              # True
print(age < 19 or (guardian and is_member))                      # True
print(score >= 90 or (attendance >= 95 and is_member))           # False
print(not is_vip and is_member and money >= 10000)               # True
print(score >= 70 and (attendance >= 80 or age >= 20))           # True
print(guardian or (not is_member and not is_vip))                # True
