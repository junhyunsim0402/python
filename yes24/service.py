import pandas as pd

def craw():
    df = pd.read_csv('./yes24/yes24_900.csv', encoding='utf-8-sig')
    
    return {
        "평균가격":    int(df['가격'].mean()),
        "최고가격":    int(df['가격'].max()),
        "최저가격":    int(df['가격'].min()),
        "최다출판연도": int(df['연도'].value_counts().idxmax()),
    }