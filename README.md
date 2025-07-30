# wood_1
우드용 리파지토리

## Weather Agent

`weather_agent.py`는 일본 기상청(JMA)과 OpenWeatherMap에서 도쿄의 날씨 정보를 수집하는 간단한 예제 스크립트입니다.

### 사용법

1. OpenWeatherMap API 키를 `OPENWEATHER_API_KEY` 환경 변수로 설정합니다.
2. 스크립트를 실행하면 JMA 예보 데이터와 OpenWeatherMap 현재 날씨 정보가 출력됩니다.

```bash
pip install requests  # 의존 패키지 설치
export OPENWEATHER_API_KEY=YOUR_API_KEY
python weather_agent.py
```
