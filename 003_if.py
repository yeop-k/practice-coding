# 003_if.py
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
else:
    print("F학점입니다.")
