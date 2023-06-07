#문제2. 이름, 국어, 영어, 수학을 입력받아 총점과 평균을 구한다
#ex 이름 : 홍길동
#   국어 : 90
#   영어 : 80
#   수학 : 80
# 홍길동님의 총점은 250이고 평균은 83.33333 입니다.

name = input("이름 : ") # 문장은 int말고 input으로 출력해야함
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

# 계산먼저 (변수에 다 넣고)
total = kor + eng + mat
avg = total/3

print(f"{name}님의 총점은 {total} 이고 평균은 {avg}")