import pandas as pd

# 예시 데이터 생성 (실제는 CSV 불러오기 등으로 대체 가능)
sales_data = pd.DataFrame({
    '거래처': ['A상사', 'B기업', 'C마트', 'D전자'],
    '매출': [500000, 300000, 150000, 400000]
})

purchase_data = pd.DataFrame({
    '거래처': ['A상사', 'B기업', 'C마트', 'D전자'],
    '매입': [200000, 320000, 100000, 450000]
})

# 매출/매입 데이터 병합
merged = pd.merge(sales_data, purchase_data, on='거래처')
merged['순매출'] = merged['매출'] - merged['매입']

# 이상거래 탐지 (매입 > 매출)
merged['이상여부'] = merged['순매출'].apply(lambda x: '⚠️ 확인 필요' if x < 0 else '')

# 결과 출력
print("📊 거래처별 매출-매입 비교 분석 결과")
print(merged)

# Excel 등 외부 저장 필요시
# merged.to_excel("sales_vs_purchase_result.xlsx", index=False)
