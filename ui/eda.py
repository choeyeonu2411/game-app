import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



def run_eda() :

    df=pd.read_csv('data/game_dataset.csv')


    st.subheader('연도별 게임 트렌드 변화')
    
    # 연도 데이터 전처리
    df['Release_Year'] = pd.to_numeric(df['Release_Year'], errors='coerce')
    df = df.dropna(subset=['Release_Year'])
    df['Release_Year'] = df['Release_Year'].astype(int)

    # 연도별 장르 집계
    genre_trends = df.groupby(['Release_Year', 'Genre']).size().unstack(fill_value=0)

    # 연도별 상위 3개 장르 추출
    top_genres = genre_trends.apply(lambda x: x.nlargest(3).index.tolist(), axis=1)

     # 시각화
    fig, ax = plt.subplots(figsize=(15, 8))
    sb.heatmap(genre_trends, cmap='YlOrRd', annot=False, ax=ax)
    ax.set_title('연도별 게임 장르 트렌드')
    ax.set_xlabel('장르')
    ax.set_ylabel('연도')
    
    st.pyplot(fig)


     # 상위 장르 출력
    st.subheader("연도별 상위 장르")

    # top_genres를 데이터프레임으로 변환하고 컬럼명 지정
    top_genres_df = top_genres.reset_index()
    top_genres_df.columns = ['Year', 'Top Genres']

    # 각 장르를 쉼표로 구분된 문자열로 변환
    top_genres_df['Top Genres'] = top_genres_df['Top Genres'].apply(lambda x: ', '.join(x))

    # 연도를 기준으로 정렬
    top_genres_df = top_genres_df.sort_values('Year', ascending=False)

    # Streamlit 테이블로 표시 (인덱스 없이)
    st.table(top_genres_df.set_index('Year'))