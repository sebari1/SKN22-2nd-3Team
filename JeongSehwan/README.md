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

본 섹션은 Spotify 사용자 데이터의 분포·특징·이탈 신호를 탐색하여, 모델링 방향과 비즈니스 인사이트 도출을 위한 근거를 제공합니다.

본 EDA는 “현실 설명”보다 **의도한 이탈 패턴이 데이터에 제대로 주입되었는지 검증**하는 것을 목표로 합니다.

원본 데이터(origin)는 변수–타깃 관계가 약해 학습이 어려웠고, 생성 데이터(generated)는 학습 가능한 신호를 만들기 위해 패턴을 주입했습니다.

## 1) 🎯 Data Overview

* **타깃(`is_churned`) 분포**를 확인해 클래스 불균형 여부 점검 
* 핵심 수치형 변수(`Offline_listening`/`ads_listening`/`subscription`)의 **분포와 특징** 파악
* Origin Data와 Generate Data 비교 후 **핵심 패턴** 파악
* 수치형 변수 간 **상관관계(히트맵)** 확인 및 중복/구조적 관계 진단

### 1.1 데이터셋 규모

* Origin: **8,000 rows × 12 columns**
* Generated: **10,000 rows × 12 columns**
* Target: `is_churned` (1=이탈, 0=유지)

### 1.2 타깃 분포(이탈률)

* Origin 이탈률: **25.89%**
* Generated 이탈률: **31.79%**

Generated는 단순히 이탈률만 바뀐 게 아니라, **이탈이 특정 조건(광고/요금제/오프라인)에서 집중**되도록 구성되어 있음.

![청취 시간 분포](./images/3-1.png)
---

## 2) ✅ Data Quality Check (Generated)

### 2.1 결측치

* 결측치 비율: **전 컬럼 0% (없음)**

### 2.2 비현실 값(음수) 존재

정규분포로 생성된 변수에서 일부 음수 발생:

* `listening_time < 0` : **18건 (0.18%)**
* `songs_played_per_day < 0` : **228건 (2.28%)**

![청취 시간 분포](./images/2-1.png)
![일일 재생 곡 수 분포](./images/2-2.png)

---

## 3) 🎯 핵심 패턴 검증 결과(Generated vs Origin)

### 3.0 Origin과 Generated 데이터의 차이
---
- **Origin 데이터(원본)**: 실제/제공된 원본 형태로, 변수들과 `is_churned(이탈)` 사이의 관계가 약해 **모델이 학습할 신호가 거의 없는 상태**였다.
- **Generated 데이터(생성/합성)**: 학습이 가능하도록, “이탈이 발생할 법한 시나리오(가정)”를 반영해 **특정 변수 조건에서 이탈 확률이 높아지도록 패턴을 주입**한 데이터이다.


---

### 3.1 요금제(subscription_type)별 이탈률
---
요금제는 현실에서도 “지불 의사/서비스 충성도”를 가장 직접적으로 반영하는 변수 중 하나다.

따라서 생성 데이터에서 **유료 고객은 이탈이 낮다**라는 가정이 실제로 구현됐는지 확인한다.

---
### Origin (차이 약함)

* Free: **24.93%**
* Premium: **25.06%**
* Student: **26.19%**
* Family: **27.52%**
>요금제를 바꿔가며 봐도 이탈률이 25~28% 수준으로 비슷하다.
즉, “요금제만 보고 이탈을 예측하기 어렵다”.

### Generated (차이 매우 큼)

* Free: **46.33%** (n=5,942 / 59.4%)
* Student: **26.57%** (n=1,020 / 10.2%)
* Premium: **5.10%** (n=3,038 / 30.4%)
>Free는 이탈이 크게 높고(약 46%), Premium은 매우 낮다(약 5%).
즉, Generated에서는 **요금제가 이탈을 ‘가르는 핵심 신호’로 의도대로 동작**한다.


![요금제별 이탈률(Origin vs Generated)](./images/fig04_subscription_churn_compare.png)

---

### 3.2 오프라인 사용(offline_listening) 여부
---
오프라인 사용은 보통 “서비스에 대한 **활용도/몰입도**”로 해석할 수 있다.

그래서 생성 데이터에서 **offline=1이 이탈을 낮추는 보호 요인**으로 주입된 가정을 검증한다.

---
### Origin

* offline=0: **24.93%**
* offline=1: **26.21%** (차이 미미)

>오프라인 사용 여부가 달라도 이탈률이 거의 비슷하다.
즉, 원본 데이터에선 오프라인 사용이 이탈을 설명하는 힘이 약하다.
### Generated

* offline=0: **45.59%** (n=5,012 / 50.1%)
* offline=1: **17.92%** (n=4,988 / 49.9%)
>오프라인을 **안 쓰는 그룹은 이탈이 높고**, **쓰는 그룹은 이탈이 낮다.**
즉, Generated에서는 offline이 **이탈 억제(보호 요인)**로 강하게 작동한다.


![오프라인 사용 여부별 이탈률(Origin vs Generated)](./images/fig05_offline_churn_compare.png)

---

### 3.3 광고 피로(ads_listened_per_week) 임계점(Threshold)
---
광고는 보통 “많을수록 조금씩 불편”이 아니라, **어느 순간부터 급격히 불만이 커지는 임계점**이 생길 수 있다.
생성 데이터에서 “광고가 일정 수준을 넘으면 이탈이 확 뛰는 구조”가 구현됐는지 확인한다.

---
Generated에서 이탈률이 **ads=15를 기준으로 급격히 달라짐**:

* ads ≤ 15: **19.15%** (n=5,342 / 53.4%)
* ads ≥ 16: **46.29%** (n=4,658 / 46.6%)
>광고가 15회를 넘는 순간, 이탈률이 **약 19% → 46%로 점프**한다.
즉, Generated에서는 광고가 **선형(조금씩 증가)**이 아니라 **임계점 이후 급증** 형태로 작동한다.

Origin은 동일 기준에서 차이가 거의 없음:

* ads ≤ 15: **25.96%**
* ads ≥ 16: **25.60%**
>원본 데이터에선 광고가 많아도 이탈이 크게 변하지 않는다.
즉, 광고 변수는 Origin에서 학습 신호가 약하다.


![광고 노출 수 분포](./images/fig06_ads_dist.png)
![광고 노출 수별 이탈률(선/막대)](./images/fig07_ads_churn_by_value.png)
![ads 임계점(≤15 vs ≥16) 이탈률 비교(Origin vs Generated)](./images/fig08_ads_threshold_compare.png)

> Origin은 세 변수(요금제/오프라인/광고)에서 이탈률 차이가 작아 “이탈을 나눌 기준”이 약했다.
> 
> 
> 반면 Generated는 같은 변수들이 이탈을 뚜렷하게 나누며, 이는 데이터 생성 시 주입한 가정이 **의도대로 구현되었음을 의미**한다.
>
---

## 4) 📈 상호작용(Interaction)

### 5.1 요금제 × 오프라인

>Generated churn rate:

* Free: `offline=0` **66.33%**, `offline=1` **26.26%**
* Student: `offline=0` **46.67%**, `offline=1` **6.47%**
* Premium: `offline=0` **4.78%**, `offline=1` **5.42%**



* Free/Student는 **offline 여부에 따라 이탈률이 크게 출렁임**
* Premium은 이미 낮은 이탈률이라 offline 효과가 상대적으로 약함


![요금제×오프라인 이탈률 히트맵](./images/fig09_sub_offline_heatmap.png)
---

## 5) 🔥 상관관계 분석 (Correlation Heatmap)

- 수치형 변수 간 상관관계를 통해 **중복 변수/구조적 관계**를 점검
- `user_id`는 수치형이더라도 의미 없는 식별자이므로 **상관관계 계산에서 제외**

### 핵심 인사이트

1. **ads_listened_per_week ↔ offline_listening 사이에 구조적 관계가 관찰됨**
- `offline_listening`은 **Premium(유료) 기능 사용 가능 여부**를 반영하는 성격이 강함
- `ads_listened_per_week`는 **Free 유저의 광고 노출(광고 피로)** 특성을 반영
    
    → 즉, 두 변수는 “서로 독립적인 행동 신호”라기보다 **구독 구조(subscription_type)의 결과로 함께 결정되는 변수**일 수 있음
    
1. **offline_listening ↔ 이탈 여부(is_churned)에서 음의 상관이 관찰됨(≈ -0.30)**
- 음의 상관은 “오프라인 사용(1)이 증가할수록 이탈(1)이 감소하는 방향”을 의미
    
    → 즉, `offline_listening`은 단순 사용 여부를 넘어 **이탈을 낮추는 보호 요인(Protective factor)**처럼 동작하는 패턴이 존재

![상관관계 히트맵](./images/6-1.png)

---

## 🧠 EDA 핵심 요약 (Key Insights)

* Origin 데이터는 요금제/광고/오프라인 등 주요 변수에서 **이탈률 차이가 작아 학습 신호가 약함**.
* Generated 데이터는 데이터 생성 규칙에 따라

  1. **Free & 광고 과다(>15)** 에서 이탈 급증(Threshold)
  2. **Premium 또는 offline 사용**은 이탈을 강하게 억제(Protective)
  3. 결과적으로 **세그먼트가 명확히 분리**되어 모델 학습에 유리한 구조를 가짐
---
