# 🎵 Spotify Churn Insight AI (SKN22-2nd-3Team)

> **스포티파이 사용자 이탈 예측 및 비즈니스 인사이트 제공 대시보드** > 사용자의 행동 패턴을 분석하여 이탈 가능성을 사전에 예측하고, 맞춤형 방어 전략을 제시합니다.

## 📌 프로젝트 개요 (Overview)
이 프로젝트는 음악 스트리밍 서비스 Spotify의 사용자 데이터를 머신러닝(ML)과 딥러닝(DL) 모델로 분석합니다.  
단순한 예측을 넘어, **'누가', '왜' 이탈하는지**를 설명하고 이를 막기 위한 **비즈니스 액션 플랜**을 제안하는 AI 웹 애플리케이션입니다.

## 👥 팀원 및 역할 (Members)
| 이름 | 역할 | 담당 업무 |
| :--- | :--- | :--- |
| **이신재** | 🎨 UI 구현 | Streamlit 웹 대시보드 기획 및 프론트엔드 구현, 시각화 |
| **장완식** | 🧠 모델 학습 | 머신러닝(RandomForest, XGBoost) 및 딥러닝 모델 설계 및 튜닝 |
| **구연미** | 🛠 데이터 전처리 | 결측치/이상치 처리, 파생 변수 생성, 데이터 스케일링 |
| **정세환** | 📊 EDA | 탐색적 데이터 분석, 상관관계 분석 및 주요 특징 도출 |

## 🚀 주요 기능 (Key Features)
1.  **모델 성능 비교 대시보드**: 다양한 AI 모델의 정확도와 F1-Score 비교 분석
2.  **실전 이탈 예측**: 사용자 정보를 입력하면 실시간으로 이탈 확률(%) 예측
3.  **심층 원인 분석**: 레이더 차트와 상세 리포트를 통해 이탈 위험 요인(Risk Factor) 시각화
4.  **비즈니스 전략 가이드**: 예측된 위험도(안전/주의/위험)에 따른 구체적인 마케팅/서비스 개선 전략 제안

## 📂 데이터셋 설명 (Data Dictionary)
이 데이터셋은 Spotify 사용자의 인구통계 정보, 이용 행태, 구독 정보 등을 포함하며, **이탈 여부(`is_churned`)**를 예측하는 것이 핵심 목표입니다.

| 구분 | 컬럼명 (Feature) | 설명 | 데이터 타입 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **식별자** | `user_id` | 사용자 고유 ID | String | 모델 학습 시 제외 |
| **유저 정보** | `gender` | 성별 (Male, Female, Other) | Categorical | |
| | `age` | 나이 | Numeric | |
| | `country` | 국가 / 지역 | Categorical | |
| **구독 정보** | `subscription_type` | 구독 요금제 유형 | Categorical | Free, Premium, Family, Student |
| **활동성** | `listening_time` | 하루 평균 청취 시간 (분) | Numeric | 서비스 몰입도 지표 |
| | `songs_played_per_day`| 하루 재생 곡 수 | Numeric | 활동량 지표 |
| | `device_type` | 주 사용 기기 | Categorical | Mobile, Desktop, Web |
| | `offline_listening` | 오프라인 모드 사용 여부 | Binary | 1: 사용, 0: 미사용 (Premium 기능) |
| **만족도/부정** | `skip_rate` | 노래 스킵 비율 (0.0 ~ 1.0) | Numeric | 높을수록 불만족 가능성 높음 |
| | `ads_listened_per_week`| 주간 광고 청취 수 | Numeric | Free 유저의 피로도 측정 지표 |
| **타겟(Target)**| `is_churned` | **이탈 여부** | Binary | **0: 유지 (Active)**<br>**1: 이탈 (Churned)** |

## 🛠 기술 스택 (Tech Stack)
* **Language**: Python 3.9+
* **Web Framework**: Streamlit
* **ML/DL**: Scikit-learn, XGBoost, TensorFlow (Keras)
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Plotly, Matplotlib, Seaborn

## 📁 프로젝트 구조 (Directory Structure)

```
SKN22-2nd-3Team/
├── data/                  # 원본 및 전처리된 데이터
├── models/                # 학습된 모델 (.pkl, .h5) 및 전처리기
├── notebooks/             # 데이터 분석 및 모델 학습 노트북 (ipynb)
├── app.py                 # Streamlit 메인 애플리케이션
└── README.md              # 프로젝트 설명 파일
```

## 📊 탐색적 데이터 분석 (EDA)

> 본 섹션은 Spotify 사용자 데이터의 분포·특징·이탈 신호를 탐색하여, 모델링 방향과 비즈니스 인사이트 도출을 위한 근거를 제공합니다.

### 1) 🎯 분석 목표

* **타깃(`is_churned`) 분포**를 확인해 클래스 불균형 여부 점검 
* 핵심 수치형 변수(청취/활동/만족도)의 **분포와 특징** 파악
* `subscription_type`, `device_type`, `country` 등 **범주형 변수별 이탈률** 비교
* 수치형 변수 간 **상관관계(히트맵)** 확인 및 중복/구조적 관계 진단

---

### 2) ✅ 데이터 검증 (Data Validation)

* 결측치/중복 여부 점검 (전처리 완료 데이터 기준)
* 식별자 `user_id`는 모델 입력에서 제외 (분석 시에도 상관관계 계산에서 제외) 

---

### 3) 🎯 타깃 분포 확인 (Class Imbalance)

* `is_churned`(이탈 여부) 분포 확인 결과, **유지(0)** 비중이 더 높아 **클래스 불균형이 존재**
* 따라서 모델 평가지표는 Accuracy 단독보다 **ROC-AUC / PR-AUC / F1** 중심 평가가 적합 

![타깃 분포(이탈/유지)](/images/3-1.png)
---

### 4) 📈 수치형 변수 분포 (Histogram)

분석 대상(전처리 데이터 기준):

* `listening_time` : 하루 평균 청취 시간(분) 
* `songs_played_per_day` : 하루 재생 곡 수 
* `skip_rate` : 스킵 비율(0~1) 
* `age` : 나이 

**주요 관찰**

* 전반적으로 분포가 크게 치우치지 않으며, **특정 단일 변수의 값만으로 이탈을 강하게 분리하기는 어려운 형태**
* `skip_rate`는 만족도/불만족의 대표 지표로, **이탈과의 관계 가능성(가설)** 을 확인하기 위해 분포 비교가 중요 

![종합히스토그램](/images/4-1.png)
![skip_rate 분포(이탈/유지)](/images/4-2.png)
![listening_time 분포(이탈/유지)](/images/4-3.png)

---

### 5) 🧩 범주형 변수별 이탈률 비교 (Churn Rate by Category)

대상:

* `subscription_type` : Free / Premium / Family / Student 
* `device_type` : Mobile / Desktop / Web 
* `country` : 국가/지역 

**주요 관찰**

* 구독 유형/기기/국가별로 이탈률 차이는 존재하지만, **결정적으로 큰 격차보다는 “소폭 차이” 중심**
* 국가(`country`)는 범주 수가 많아 **사용자 수 상위 국가만 추려** 가독성 있게 비교

![구독 유형별 이탈율](/images/5-1-1.png)
![사용 기기별 이탈율](/images/5-2.png)
![국가별 이탈율](/images/5-3.png)

---

### 6) 🔥 상관관계 분석 (Correlation Heatmap)

* 수치형 변수 간 상관관계를 통해 **중복 변수/구조적 관계**를 점검
* `user_id`는 수치형이더라도 의미 없는 식별자이므로 **상관관계 계산에서 자동 제외** 

**핵심 인사이트**

* `ads_listened_per_week` ↔ `offline_listening` 사이에 **강한 구조적 관계**가 관찰됨

  * `offline_listening`은 Premium 기능(유료) 여부를 반영 
  * `ads_listened_per_week`는 Free 유저 특성(광고 피로도) 반영 
    → 즉, 두 변수는 행동 독립 신호라기보다 **구독 구조(subscription_type)의 결과 변수**로 중복 정보가 될 수 있음

![상관관계 히트맵](/images/6-1.png)

---

## 🧠 EDA 핵심 요약 (Key Insights)

1. **클래스 불균형 존재** → F1/ROC-AUC/PR-AUC 중심 평가 권장
2. 수치형 변수의 분포는 전반적으로 완만하며, **단일 변수로 강한 분리 신호는 제한적**
3. `subscription_type`, `device_type`, `country`는 **세그먼트 관점 차이는 있으나** 큰 격차보다는 보조 신호 성격
4. `ads_listened_per_week`와 `offline_listening`은 **구독 구조로 인해 중복 정보 가능성** → 모델 입력 시 조합/중복 제거 전략 필요

---
