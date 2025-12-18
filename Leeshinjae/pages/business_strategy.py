import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Spotify Business Strategy",
    page_icon="🎧",
    layout="wide"
)

# 2. 스포티파이 컨셉 커스텀 CSS
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #121212 !important;
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    .main-title { 
        font-size: 42px; 
        font-weight: 800; 
        color: #FFFFFF;
        margin-bottom: 5px; 
    }
    .sub-title { 
        font-size: 24px; 
        font-weight: 700; 
        color: #1DB954; 
        margin-top: 5px;
        margin-bottom: 30px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #121212;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #282828;
        border-radius: 4px;
        color: #B3B3B3;
        padding: 0px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1DB954 !important;
        color: #FFFFFF !important;
    }
    .strategy-card {
        background-color: #181818;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 25px;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .strategy-card:hover {
        background-color: #282828;
        border-color: #1DB954;
    }
    .card-header {
        font-size: 22px;
        font-weight: 700;
        color: #1DB954;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .card-content {
        color: #B3B3B3;
        line-height: 1.8;
    }
    .highlight-text {
        color: #FFFFFF;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 3. 헤더 영역
st.markdown('<div class="main-title">💡 비즈니스 전략 가이드</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">📌 AI 분석 기반 액션 플랜</div>', unsafe_allow_html=True)

# 4. 상태별 전략 (탭)
tab1, tab2, tab3, tab4 = st.tabs([
    "🔴 긴급 방어", 
    "🟡 잠재 관리", 
    "🟢 충성/수익화", 
    "⚙️ 서비스 개선"
])

with tab1:
    st.markdown('### <span style="color:#FF4B4B">🚨 이탈 확률 70% 이상: 즉각적인 개입 필요</span>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="strategy-card">
            <div class="card-header">💰 가격 방어 전략</div>
            <div class="card-content">
                • <span class="highlight-text">시크릿 오퍼:</span> 3개월 50% 할인 쿠폰 즉시 푸시 발송<br>
                • <span class="highlight-text">다운그레이드 제안:</span> 해지 대신 '광고형 무료 요금제' 유지 유도
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="strategy-card">
            <div class="card-header">🎧 콘텐츠 심폐소생</div>
            <div class="card-content">
                • <span class="highlight-text">향수 마케팅:</span> 'OO님이 2년 전 가장 많이 들었던 곡' 리스트 생성<br>
                • <span class="highlight-text">큐레이션 리셋:</span> 기존 추천 알고리즘 초기화 옵션 제공
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown('### <span style="color:#FFD700">⚠️ 이탈 확률 40~70%: 골든타임 관리</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="strategy-card">
        <div class="card-header">📍 Silent Churn 방지 액션</div>
        <div class="card-content">
            • <span class="highlight-text">광고 피로도 관리:</span> Free 유저 대상 광고 노출 빈도 30% 일시 축소<br>
            • <span class="highlight-text">기능 튜토리얼:</span> '데이터 절약 모드', '오프라인 저장' 기능 팝업 안내<br>
            • <span class="highlight-text">푸시 알림 최적화:</span> 선호 아티스트 신곡 알림 위주의 선별 발송
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('### <span style="color:#1DB954">💎 이탈 확률 40% 미만: 수익 극대화 및 락인</span>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="strategy-card">
            <div class="card-header">💸 Upselling</div>
            <div class="card-content">
                • <span class="highlight-text">패밀리/듀오 요금제:</span> '친구와 함께 쓰면 반값' 프로모션 노출<br>
                • <span class="highlight-text">굿즈 연계:</span> 아티스트 콘서트 티켓 우선 예매권 추첨 기회
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="strategy-card">
            <div class="card-header">🙋‍♂️ MGM (친구 추천)</div>
            <div class="card-content">
                • <span class="highlight-text">친구 초대 이벤트:</span> 초대 시 양쪽 모두에게 1개월 무료 혜택 제공<br>
                • <span class="highlight-text">마케팅 강화:</span> 가장 강력한 신규 고객 유입 채널로 활용
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown('### <span style="color:#B3B3B3">⚙️ 프로덕트 및 데이터 개선 방향</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="strategy-card">
        <div class="card-header">🔍 데이터 기반 약점 진단</div>
        <div class="card-content">
            1. <span class="highlight-text">'탐색 피로' 해결:</span> '하이라이트 미리듣기' 기능 도입 검토<br>
            2. <span class="highlight-text">광고 경험 개선:</span> 청취 흐름을 유지하는 '오디오 배너 광고' 비중 확대<br>
            3. <span class="highlight-text">초기 적응 실패:</span> 가입 첫 주 유저 대상 온보딩(Onboarding) 전면 개편
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. 푸터 (에러가 자주 발생하는 지점)
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("© 2025 Spotify Churn Analytics Dashboard")