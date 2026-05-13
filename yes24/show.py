import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import koreanfont

df = pd.read_csv('./yes24/yes24_900.csv', encoding='utf-8')

avg_price  = int(df['가격'].mean())
max_price  = int(df['가격'].max())
min_price  = int(df['가격'].min())
year_count = df['연도'].value_counts().sort_index()

print("=== 가격 통계 분석 ===")
print(f"평균 가격: {avg_price:,}원")
print(f"최고 가격: {max_price:,}원")
print(f"최저 가격: {min_price:,}원")
print("\n=== 연도별 도서 수 ===")
print(year_count)

plt.figure(figsize=(10, 5))
plt.hist(df['가격'], bins=10, color='blue')
plt.title('가격 분포')
plt.xlabel('가격 (원)')
plt.ylabel('도서 수')
 
# 가격대별 도서 개수 출력
bins = range(0, df['가격'].max() + 5000, 5000)
df['가격대'] = pd.cut(df['가격'], bins=bins)
print("\n=== 가격대별 도서 개수 ===")
print(df['가격대'].value_counts().sort_index())
 
plt.tight_layout()
plt.savefig('./yes24/price_histogram.png')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(year_count.index.astype(str), year_count.values, color='coral', edgecolor='white')
plt.title('연도별 출판 도서 수')
plt.xlabel('출판 연도')
plt.ylabel('도서 수')
 
plt.tight_layout()
plt.savefig('./yes24/year_bar.png', dpi=150)
plt.show()