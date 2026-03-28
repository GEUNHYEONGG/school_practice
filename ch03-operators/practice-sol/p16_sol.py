"""
실습 16 풀이: 파일 크기 표시 (삼항 연산자)
"""

size = int(input("파일 크기(바이트) 입력: "))

# 1024 이상이면 KB, 아니면 B
label = f"{size / 1024:.1f}KB" if size >= 1024 else f"{size}B"
print(f"파일 크기: {label}")
