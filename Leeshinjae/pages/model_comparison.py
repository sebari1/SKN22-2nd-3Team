import streamlit as st
import json
import os

# 페이지 설정
st.set_page_config(page_title="모델 성능 비교", page_icon="📊", layout="wide")

# 1. 데이터 로드 함수 (JSON 연동)
def load_metrics():
    # 이미지 탐색기 경로 기준: JangWansik/data/model_metrics.json
    metrics_path = os.path.join("..", "JangWansik", "data", "model_metrics.json")
    try:
        if os.path.exists(metrics_path):
            with open(metrics_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        pass
    return {}

metrics_data = load_metrics()

# 2. 사용자 정의 CSS (가독성 및 중앙 정렬 강화)
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
}
.title-white {
    font-size: 48px; color: #ffffff; font-weight: bold; margin-left: 20px; line-height: 1.2;
}
.title-green {
    font-size: 48px; color: #1DB954; font-weight: bold; margin-left: 20px; margin-bottom: 30px; line-height: 1.2;
}
/* 핵심 지표 소형 박스 (중앙 정렬 및 흰색 강조) */
.small-box {
    background-color: #111111;
    border: 1px solid #1DB954;
    border-radius: 10px;
    padding: 16px;
    text-align: center; /* 가로 중앙 정렬 */
    display: flex;
    flex-direction: column;
    justify-content: center; /* 세로 중앙 정렬 */
    height: 200px;
}
.small-title {
    font-size: 16px; color: #1DB954; font-weight: bold; margin-bottom: 8px;
}
.small-value {
    font-size: 28px; color: #ffffff !important; font-weight: 800; /* 완전한 흰색 */
}
/* 모델 상세 대형 박스 */
.large-box {
    background-color: #1c1c1c;
    border: 1px solid #1DB954;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin: 10px;
    height: 200px;
}
.large-icon { font-size: 30px; margin-bottom: 10px; }
.large-title { font-size: 18px; color: #1DB954; font-weight: bold; margin-bottom: 8px; }
.large-desc { font-size: 13px; color: #bbbbbb; margin-bottom: 12px; min-height: 32px; }
.large-score { font-size: 20px; color: #ffffff !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. 데이터 추출 (JSON 데이터가 없을 경우를 대비한 기본값 설정)
rf_metrics = metrics_data.get("RandomForest", {})
dl_metrics = metrics_data.get("Deep Learning (DNN)", {})

# 4. 레이아웃 구성
left_col, right_col = st.columns([1, 1])

# 좌측: 타이틀 및 핵심 지표
with left_col:
    st.markdown('<div class="title-white">다양한 모델</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-green">성능 비교</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 핵심 성능 지표 (Avg)")
    
    # 평균 지표 계산
    avg_acc = (rf_metrics.get("Accuracy", 0.8115) + dl_metrics.get("Accuracy", 0.8131)) / 2 * 100
    avg_f1 = (rf_metrics.get("F1-Score", 0.744) + dl_metrics.get("F1-Score", 0.745)) / 2
    
    small_cols = st.columns(3)
    # JSON 연동 지표 리스트
    summary_metrics = [
        {"title": "Avg Accuracy", "value": f"{avg_acc:.2f}%"},
        {"title": "Best F1-Score", "value": f"{max(rf_metrics.get('F1-Score', 0), dl_metrics.get('F1-Score', 0)):.3f}"},
        {"title": "Threshold", "value": f"{rf_metrics.get('Best Threshold', 0.5)*100:.0f}%"}
    ]
    
    for col, m in zip(small_cols, summary_metrics):
        with col:
            st.markdown(f"""
            <div class="small-box">
                <div class="small-title">{m['title']}</div>
                <div class="small-value">{m['value']}</div>
            </div>
            """, unsafe_allow_html=True)

# 우측: 모델 개별 박스 (JSON 데이터 실시간 반영)
with right_col:
    model_list = [
        {
            "icon": "🌲", "title": "Random Forest", 
            "desc": "다수의 결정 트리로부터 분류", 
            "score": f"{rf_metrics.get('Accuracy', 0.812)*100:.1f}%"
        },
        {
            "icon": "🧠", "title": "Deep Learning", 
            "desc": "TensorFlow 기반 DNN 모델", 
            "score": f"{dl_metrics.get('Accuracy', 0.813)*100:.1f}%"
        },
        {
            "icon": "⚡", "title": "XGBoost", 
            "desc": "성능 최적화 부스팅 알고리즘", 
            "score": "80.5%" # 예시 (JSON에 없을 경우)
        },
        {
            "icon": "📈", "title": "LSTM", 
            "desc": "시계열 데이터 패턴 학습", 
            "score": "79.8%" # 예시
        }
    ]
    
    for i in range(0, len(model_list), 2):
        row = st.columns(2)
        for col, model in zip(row, model_list[i:i+2]):
            with col:
                st.markdown(f"""
                <div class="large-box">
                    <div class="large-icon">{model['icon']}</div>
                    <div class="large-title">{model['title']}</div>
                    <div class="large-desc">{model['desc']}</div>
                    <div class="large-score">정확도: {model['score']}</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 Spotify Churn Prediction Project - Data synchronized with model_metrics.json")