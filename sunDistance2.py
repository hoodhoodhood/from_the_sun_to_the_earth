import ephem

# 현재 위치 위도와 경도
latitude = '35.169033'
longitude = '128.081845'

# ephem Observer 객체 생성
obs = ephem.Observer()
obs.lat, obs.lon = latitude, longitude

# 현재 시간 설정
obs.date = ephem.now()

# 태양 객체 생성
sun = ephem.Sun()

# 태양과의 거리 계산
sun.compute(obs)
distance_au = sun.earth_distance
distance_km = distance_au * 149597870.7

print("태양과의 거리(단위: km):", distance_km)