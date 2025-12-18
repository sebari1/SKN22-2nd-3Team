import streamlit as st
import plotly.graph_objects as go
import json
import os

# 페이지 설정
st.set_page_config(page_title="피처 중요도", page_icon="📊", layout="wide")

# 1. JSON 데이터 로드 함수 (경로: ../JangWansik/data/model_metrics.json)
def load_metrics():
    # 파일 탐색기 이미지 구조에 따른 경로 설정
    metrics_path = os.path.join("..", "JangWansik", "data", "model_metrics.json")
    try:
        if os.path.exists(metrics_path):
            with open(metrics_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        st.error(f"데이터를 불러오는데 실패했습니다: {e}")
    return {}

metrics_data = load_metrics()

# 2. 사용자 정의 CSS (중앙 정렬 및 흰색 텍스트 강조)
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
}
.title {
    text-align: center; font-size: 48px; font-weight: bold; color: #ffffff; margin-bottom: 0px;
}
.subtitle {
    text-align: center; font-size: 20px; color: #1DB954; margin-bottom: 40px;
}
/* 상단 핵심 지표 박스 스타일 */
.metric-container {
    background-color: #111111;
    border: 1px solid #1DB954;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin-bottom: 30px;
}
.metric-label {
    color: #b3b3b3; font-size: 14px; margin-bottom: 8px;
}
.metric-value {
    color: #ffffff !important; font-size: 32px; font-weight: 800;
}
.footer {
    text-align: center; font-size: 14px; color: #888888; margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# 타이틀 및 서브타이틀
st.markdown('<div class="title">피처 중요도</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ML/DL 기반 고객 이탈 예측 프로젝트</div>', unsafe_allow_html=True)

# 3. 상단 핵심 지표 섹션 (JSON 연동)
if metrics_data:
    rf_acc = metrics_data.get("RandomForest", {}).get("Accuracy", 0) * 100
    dl_acc = metrics_data.get("Deep Learning (DNN)", {}).get("Accuracy", 0) * 100
    avg_acc = (rf_acc + dl_acc) / 2
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-container"><div class="metric-label">평균 모델 정확도</div><div class="metric-value">{avg_acc:.1f}%</div></div>', unsafe_allow_html=True)
    with col2:
        max_f1 = max(metrics_data.get("RandomForest", {}).get("F1-Score", 0), 
                     metrics_data.get("Deep Learning (DNN)", {}).get("F1-Score", 0))
        st.markdown(f'<div class="metric-container"><div class="metric-label">최고 F1-Score</div><div class="metric-value">{max_f1:.3f}</div></div>', unsafe_allow_html=True)
    with col3:
        threshold = metrics_data.get("RandomForest", {}).get("Best Threshold", 0.5) * 100
        st.markdown(f'<div class="metric-container"><div class="metric-label">최적 임계값</div><div class="metric-value">{threshold:.1f}%</div></div>', unsafe_allow_html=True)

# 4. 피처 중요도 차트
st.markdown("### 📊 주요 영향 인자 분석")
# 피처 데이터 (이 부분은 필요 시 별도의 CSV나 JSON 키로 분리 가능)
features = ["구독 타입", "오프라인 재생", "광고 청취시간", "음악 재생시간", "나라", "만족도 지수"]
importance = [48.7, 21.5, 19.2, 2.4, 1.8, 1.7]

fig = go.Figure(go.Bar(
    x=features,
    y=importance,
    marker_color='#1DB954',
    text=[f"{v}%" for v in importance],
    textposition="outside"
))
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#ffffff"),
    xaxis=dict(tickfont=dict(color="#ffffff")),
    yaxis=dict(range=[0, 110], showgrid=False, visible=False), # 깔끔한 뷰를 위해 y축 숨김
    margin=dict(t=40, b=40, l=40, r=40),
    height=450
)

st.plotly_chart(fig, use_container_width=True)

# 하단 설명
st.markdown('<div class="footer">Spotify Churn Prediction<br>© 2024 Customer Churn Prediction Project</div>', unsafe_allow_html=True)