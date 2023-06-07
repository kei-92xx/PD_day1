# -*- coding: utf-8 -*-
#문제1:주급계산하기, 근무시간(30), 시간당급여액(15000)

work_time = input("근무시간 : ")
per_pay = input("시간당급여액 : ") 
pay = int(work_time) * int(per_pay)

print("주급은", pay, "입니다")
#파이썬의 경우는 문자열과 다른타입을 + 연산을 못함
#형전환; 형을 바꾼다. int(다른타입을 > int로), str(다른타입을 > str)
print("주급은 " + str(pay) + "입니다")

#문자열과 숫자를 섞어서 출력하고자 할때
# %d - decimal(숫자)
# 예전거 - 웹프로그램, 디비에 데이터 읽고 쓸때
print(str.format("주급은 %d 입니다"  % pay))
print(f"주급은 {pay} 입니다") #fstring 3.6부터 문자열앞에 f를 쓴다
