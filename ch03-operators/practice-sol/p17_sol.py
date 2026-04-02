"""
실습 17 풀이: 점수 처리 프로그램
"""

# 1. 각 점수를 입력받아 변수에 저장
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
math = int(input("수학 점수: "))

# 2. 다중 대입으로 과목명을 한 줄에 저장
sub1, sub2, sub3 = "국어", "영어", "수학"

# 3. total을 0으로 초기화
total = 0

# 4. +=로 총점 누적
total += kor
total += eng
total += math

# 5. 평균 계산 (총점 / 과목 수)
average = total / 3

# 결과 출력
print("과목:", sub1, sub2, sub3)
print(sub1 + ":", kor)
print(sub2 + ":", eng)
print(sub3 + ":", math)
print("총점:", total)
print("평균:", average)
