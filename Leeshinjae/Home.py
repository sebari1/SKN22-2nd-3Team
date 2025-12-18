import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Spotify 고객 이탈 예측",
    page_icon="🎧",
    layout="wide"
)

# 2. 사용자 정의 CSS
st.markdown("""
<style>
/* 배경 및 기본 텍스트 설정 */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
}

/* 텍스트 스타일 */
.title {
    text-align: center;
    font-size: 26px;
    color: #ffffff;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 6px;
}
.headline-white {
    text-align: center;
    font-size: 96px;
    color: #ffffff;
    font-weight: 800;
    margin: 0;
    line-height: 1.2;
}
.headline-green {
    text-align: center;
    font-size: 96px;
    color: #1DB954;
    font-weight: 800;
    margin: 2px 0 12px 0;
    line-height: 1.2;
}

/* 버튼 스타일: 중앙 정렬을 위해 width 100% 설정 */
div.stButton > button:first-child {
    background:#7B3FE4; 
    color:white;
    border:none;
    border-radius:8px;
    padding:16px 28px;
    font-size:18px;
    font-weight:600;
    cursor:pointer;
    width: 100%; /* 컬럼 내에서 꽉 차게 설정 */
    margin-top: 20px;
}

.description {
    color: #ffffff;
    text-align: center;
    font-size: 16px;
    margin: 30px auto 40px auto;
    max-width: 900px;
    line-height: 1.6;
}

/* 메트릭 박스 스타일 */
.metric {
    background-color: #111111;
    border: 1px solid #1DB954;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.metric-title {
    font-size: 24px;
    color: #1DB954;
    font-weight: 700;
    margin-bottom: 6px;
}
.metric-desc {
    font-size: 16px;
    color: #ffffff;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# 3. 메인 화면 구성
st.markdown('<div class="title">🎧 Spotify Customer Analytics 🎵</div>', unsafe_allow_html=True)
st.markdown('<div class="headline-white">가입 고객</div>', unsafe_allow_html=True)
st.markdown('<div class="headline-green">이탈 예측</div>', unsafe_allow_html=True)

# --- 버튼 중앙 배치 영역 ---
# [2, 1, 2] 비율로 컬럼을 나누어 가운데(1)에 버튼 배치
col1, col_center, col2 = st.columns([4, 1, 3])

with col_center:
    if st.button("예측하기 →", key="guide_btn"):
        # ✅ 경로 에러 해결: 반드시 'pages/파일명.py' 형식을 사용해야 합니다.
        # 파일이 실제 'pages' 폴더 안에 있는지 꼭 확인하세요!
        st.switch_page("pages/ChurnCheck.py") 
# -------------------------

# 설명 텍스트
st.markdown("""
<div class="description">
머신러닝과 딥러닝을 활용한 Spotify 고객 이탈 예측 모델 구축 및 배포 프로젝트입니다.<br>
고객 행동 데이터를 기반으로 이탈 가능성을 실시간으로 예측하여 비즈니스 전략 수립에 도움을 줍니다.
</div>
""", unsafe_allow_html=True)

# 메트릭 박스: 1행 4열
cols = st.columns(4)
metrics = [
    {"title": "ML/DL", "desc": "모델 활용"},
    {"title": "~95%+", "desc": "예측 정확도"},
    {"title": "4", "desc": "파이프라인 단계"},
    {"title": "Real-time", "desc": "배포 환경"}
]

for col, m in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric">
            <div class="metric-title">{m['title']}</div>
            <div class="metric-desc">{m['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# 푸터
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("© 2025 Spotify Churn Prediction Project")