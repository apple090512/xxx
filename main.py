import streamlit as st

st.set_page_config(page_title="게임 장르별 공략법", layout="centered")

st.title("🎮 게임 장르별 공략법")

game_guides = {
    'RPG': [
        {'name': '엘든 링', 'guide': '보스전은 패턴 분석이 핵심이며, 회피 타이밍을 익히는 것이 중요합니다.'},
        {'name': '파이널 판타지 7 리메이크', 'guide': 'ATB 게이지를 적극적으로 활용하고, 약점 속성에 맞는 마테리아를 세팅하세요.'},
    ],
    'FPS': [
        {'name': '오버워치 2', 'guide': '팀 조합과 궁극기 운영이 중요합니다. 맵 지형을 활용하세요.'},
        {'name': '콜 오브 듀티: 모던 워페어', 'guide': '소리 감지와 미니맵 활용을 통해 적 위치를 예측하세요.'},
    ],
    '액션': [
        {'name': '세키로: 섀도우 다이 트와이스', 'guide': '패링(PARRY)이 전투의 핵심입니다. 타이밍 연습이 필요합니다.'}
    ]
}

# 장르 선택
genre = st.selectbox("장르를 선택하세요", options=
