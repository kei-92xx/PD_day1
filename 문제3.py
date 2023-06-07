# 문제3. 미터를 입력받아 km와 m를 구하기
# 입력 예) 미터 : 1234
# 출력 예) 1234m 는 1km와 234m 입니다

M = int(input("미터 : "))

#계산
km = M // 1000
meter = M %1000

print(f"{M} 는 {km}km와 {meter}m입니다")
