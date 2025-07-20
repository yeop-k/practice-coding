# 007_sales_summary.py
# 간단한 매출 요약 분석기

sales_data = {
    '2025-07-15': 130000,
    '2025-07-16': 175000,
    '2025-07-17': 155000,
    '2025-07-18': 98000,
    '2025-07-19': 240000,
}

# 총매출
total = sum(sales_data.values())

# 평균 매출
average = total / len(sales_data)

# 최대/최소 매출일
max_day = max(sales_data, key=sales_data.get)
min_day = min(sales_data, key=sales_data.get)

# 출력
print("📊 매출 요약 분석 결과")
print(f"총매출: {total:,}원")
print(f"일평균 매출: {average:,.0f}원")
print(f"최고 매출일: {max_day} ({sales_data[max_day]:,}원)")
print(f"최저 매출일: {min_day} ({sales_data[min_day]:,}원)")
