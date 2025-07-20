# 006_fraud_detector.py
# 간단한 이상 거래 탐지기

# 거래 금액 리스트
transactions = [1500, 2500, 30000, 2000, 120000, 1800, 2200]

# 이상 거래 기준 (예: 1만 원 초과 시 이상 거래로 간주)
threshold = 10000

# 이상 거래 탐지
suspicious = []
for i, amount in enumerate(transactions):
    if amount > threshold:
        suspicious.append((i, amount))

# 결과 출력
print("📢 이상 거래 탐지 결과")
if not suspicious:
    print("이상 거래 없음")
else:
    for idx, amt in suspicious:
        print(f"{idx+1}번째 거래: {amt}원 (기준 초과)")
