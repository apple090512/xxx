import streamlit as st

st.set_page_config(page_title="요리 레시피 모음", layout="centered")

st.title("🍽 요리 레시피 모음")

recipe_data = {
    '서양 요리': [
        {'title': '스파게티 볼로네제', 'desc': '다진 소고기와 토마토소스를 사용한 파스타입니다.'},
        {'title': '치킨 알프레도', 'desc': '크림소스와 닭고기를 곁들인 부드러운 파스타 요리입니다.'},
        {'title': '시저 샐러드', 'desc': '로메인과 파르메산 치즈, 크루통이 들어간 고전적인 샐러드.'}
    ],
    '한식 요리': [
        {'title': '비빔밥', 'desc': '다양한 나물과 고기, 고추장을 비벼 먹는 한국 대표 음식.'},
        {'title': '불고기', 'desc': '얇게 썬 쇠고기를 간장 양념에 재운 후 볶은 요리입니다.'},
        {'title': '김치찌개', 'desc': '김치, 돼지고기, 두부 등을 넣고 끓인 찌개입니다.'}
    ]
}

for category, recipes in recipe_data.items():
    st.header(category)
    for recipe in recipes:
        st.subheader(recipe['title'])
        st.write(recipe['desc'])
        st.markdown("---")
