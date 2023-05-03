import math
import datetime

# 현재 위치의 GPS 좌표 (경도, 위도)
longitude = 128.081845  # 경도
latitude = 35.169033   # 위도

# 1. 현재 시간으로부터 2000년 1월 1일 12시까지의 일 수를 구합니다.
now = datetime.datetime.utcnow() # UTC (협정 세계시)로 현재 날짜와 시간을 가져온다.  한국 시간은 UTC+9 이므로 해당 시간에 9시간을 더해주면 한국시간을 알 수 있다.
days_since_2000 = (now - datetime.datetime(2000, 1, 1, 12, 00, 00)).days # 2000년 1월 1일 12시는 윤초를 고려한 협정 세계시(UTC)와 기원전 2000년 대략적인 태양의 위치를 맞추기 위한 표준 기준 시간입니다.

# 2. 태양의 평균 궤도 경도를 계산합니다.
mean_longitude = (280.460 + 0.9856474 * days_since_2000) % 360

# 3. 태양의 평균 균일 경도를 계산합니다.
mean_anomaly = (357.528 + 0.9856003 * days_since_2000) % 360
print(mean_anomaly)

# 4. 태양의 이심률, 궤도 경도, 평균 균일 경도를 이용하여 진실 균일 경도를 계산합니다.
eccentricity = 0.016709 - 0.000042 * days_since_2000 # 이심률은 물체의 운동이 원운동에서 벗어난 정도를 나타낸다.
true_anomaly = mean_anomaly + 1.914 * math.sin(math.radians(mean_anomaly)) + \
               0.02 * math.sin(math.radians(2 * mean_anomaly)) 
true_longitude = mean_longitude + 1.915 * math.sin(math.radians(true_anomaly)) + \
                 0.02 * math.sin(math.radians(2 * true_anomaly))

# 5. 태양의 적위, 자오선 거리, 시각각 거리를 계산합니다.
obliquity = 23.439 - 0.0000004 * days_since_2000
y = math.sin(math.radians(true_longitude)) * math.cos(math.radians(obliquity))
x = math.cos(math.radians(true_longitude))
right_ascension = math.degrees(math.atan2(y, x))
declination = math.degrees(math.asin(math.sin(math.radians(obliquity)) * \
                 math.sin(math.radians(true_longitude))))
earth_sun_distance = (1 - eccentricity ** 2) / (1 + eccentricity * math.cos(math.radians(true_anomaly)))
hour_angle = math.radians(15 * (now.hour - 12) + now.minute / 4 + longitude - right_ascension)
altitude = math.degrees(math.asin(math.sin(math.radians(latitude)) * math.sin(math.radians(declination)) + \
              math.cos(math.radians(latitude)) * math.cos(math.radians(declination)) * math.cos(hour_angle)))
zenith_angle = 90 - altitude
earth_sun_distance *= 149.6e6

# 6. 태양과의 거리를 출력합니다.
print(f"태양과 현재 위치의 거리는 약 {earth_sun_distance:.0f} km 입니다.")