import streamlit as st

# 지역별 다수 요리 레시피 데이터
recipes = {
    "서양": [
        {
            "요리명": "스파게티 카르보나라",
            "재료": ["스파게티 면", "베이컨", "계란 노른자", "파마산 치즈", "후추"],
            "조리법": [
                "스파게티 면을 삶는다.",
                "베이컨을 잘게 썰어 팬에 볶는다.",
                "계란 노른자와 파마산 치즈를 섞어 소스를 만든다.",
                "삶은 면과 베이컨, 소스를 섞고 후추로 간한다."
            ]
        },
        {
            "요리명": "치즈버거",
            "재료": ["햄버거 번", "소고기 패티", "치즈", "양상추", "토마토", "케첩"],
            "조리법": [
                "패티를 구운다.",
                "번에 양상추, 토마토, 패티, 치즈를 올린다.",
                "케첩을 뿌려서 완성한다."
            ]
        },
        {
            "요리명": "시저 샐러드",
            "재료": ["로메인 상추", "크루통", "파마산 치즈", "시저 드레싱"],
            "조리법": [
                "상추를 씻고 잘게 자른다.",
                "크루통과 치즈를 뿌린다.",
                "시저 드레싱을 뿌려 섞는다."
            ]
        },
    ],
    "동양": [
        {
            "요리명": "비빔밥",
            "재료": ["밥", "나물", "고추장", "계란", "참기름"],
            "조리법": [
                "밥을 그릇에 담는다.",
                "나물을 올린다.",
                "계란 프라이를 올린다.",
                "고추장과 참기름을 넣고 비벼서 먹는다."
            ]
        },
        {
            "요리명": "된장찌개",
            "재료": ["된장", "두부", "호박", "감자", "양파", "대파"],
            "조리법": [
                "물에 된장을 풀고 끓인다.",
                "채소와 두부를 넣고 익힌다.",
                "대파를 넣고 한소끔 더 끓인다."
            ]
        },
        {
            "요리명": "잡채",
            "재료": ["당면", "시금치", "당근", "버섯", "간장", "참기름"],
            "조리법": [
                "당면을 삶는다.",
                "채소를 볶는다.",
                "당면과 채소를 간장과 참기름에 버무린다."
            ]
        },
    ],
    "북미": [
        {
            "요리명": "치킨 윙",
            "재료": ["닭 날개", "핫소스", "버터", "소금", "후추"],
            "조리법": [
                "닭 날개에 소금과 후추로 밑간한다.",
                "오븐에서 굽거나 튀긴다.",
                "핫소스와 버터를 섞은 소스를 바른다."
            ]
        },
        {
            "요리명": "클램 차우더",
            "재료": ["조개", "감자", "양파", "생크림", "베이컨"],
            "조리법": [
                "베이컨을 볶는다.",
                "양파와 감자를 넣고 끓인다.",
                "조개와 생크림을 넣고 완성한다."
            ]
        },
        {
            "요리명": "BBQ 립",
            "재료": ["돼지갈비", "바비큐 소스", "소금", "후추"],
            "조리법": [
                "돼지갈비에 소금, 후추로 간한다.",
                "오븐이나 그릴에 바비큐 소스를 바르며 굽는다."
            ]
        },
    ],
}

# 커스텀 CSS for ul 스타일링
st.markdown(
    """
    <style>
    .fancy-list {
        list-style-type: square;
        padding-left: 20px;
        color: #d2691e;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
    }
    .fancy-list li {
        margin-bottom: 8px;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("세계 요리 레시피")

region = st.selectbox("지역을 선택하세요", options=list(recipes.keys()))

if region:
    st.header(f"{region} 요리 리스트")
    for recipe in recipes[region]:
        st.subheader(recipe["요리명"])
        st.markdown("**재료:**")
        # 화려한 ul 스타일링
        ingredients_html = "<ul class='fancy-list'>" + "".join([f"<li>{i}</li>" for i in recipe["재료"]]) + "</ul>"
        st.markdown(ingredients_html, unsafe_allow_html=True)

        st.markdown("**조리법:**")
        steps_html = "<ul class='fancy-list'>" + "".join([f"<li>{step}</li>" for step in recipe["조리법"]]) + "</ul>"
        st.markdown(steps_html, unsafe_allow_html=True)
