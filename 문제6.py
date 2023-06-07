#문제6. 동전 거스르기
#거스름돈 : 78767
#  50000 - 1장, 10000 - 2장, 5000 - 1장, 1000 - 3장, 500 - 1개, 100 - 2개, 50 - 1개, 10 - 1개

#입력 : 78767

money = int(input("거스름돈 : "))
temp = money #원금액을 보존하려고 임시 변수 만들어서 값을 저장

m50000 = temp // 50000
temp = temp % 50000   #나머지만 28760원 남음
m10000 = temp // 10000
temp = temp % 10000
m5000 = temp // 5000
temp = temp % 5000
m1000 = temp // 1000
temp = temp % 1000
m500 = temp // 500
temp = temp % 500
m100 = temp // 100
temp = temp % 100
m50 = temp // 50
temp = temp % 50
m10 = temp // 10
temp = temp % 10

print(f'50000 -> {m50000}장')
print(f'10000 -> {m10000}장')
print(f' 5000 -> {m5000}장' )
print(f' 1000 -> {m1000}장' )
print(f'  500 -> {m500}개'  )
print(f'  100 -> {m100}개'  )
print(f'   50 -> {m50}개'   )
print(f'   10 -> {m10}개'   )