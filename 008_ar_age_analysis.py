# 008_ar_age_analysis.py
# 외상매출금 연령 분석기

from datetime import datetime

# 가상의 외상매출금 데이터 (거래처명, 청구일, 금액)
ar_data = [
    ("고객A", "2024-12-15", 1_200_000),
    ("고객B", "2025-01-30", 850_000),
    ("고객C", "2025-03-10", 430_000),
    ("고객D", "2025-06-15", 500_000),
    ("고객E", "2025-07-10", 300_000),
]

# 분석 기준일
today = datetime.strptime("2025-07-20", "%Y-%m-%d")

# 연령대별 그룹핑
aging_buckets = {
    "0~30일": 0,
    "31~60일": 0,
    "61~90일": 0,
    "90일 초과": 0,
}

for customer, date_str, amount in ar_data:
    invoice_date = datetime.strptime(date_str, "%Y-%m-%d")
    days = (today - invoice_date).days

    if days <= 30:
        aging_buckets["0~30일"] += amount
    elif days <= 60:
        aging_buckets["31~60일"] += amount
    elif days <= 90:
        aging_buckets["61~90일"] += amount
    else:
        aging_buckets["90일 초과"] += amount

# 출력
print("📊 외상매출금 연령 분석 결과")
for bucket, total in aging_buckets.items():
    print(f"{bucket}: {total:,}원")
