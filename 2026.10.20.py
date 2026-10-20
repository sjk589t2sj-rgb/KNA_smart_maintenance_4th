print("안녕하세요!")
print(75)

# 형식: print(값)
# - print는 파이썬에 기본으로 들어있는 "내장 함수"
# - 괄호 안에 넣은 값을 화면에 그대로 출력

# 여러 번 쓰면 여러 줄로 나옴 (print 한 번 =한 줄)
print("첫번째 줄")
print("두번째 줄")
# 숫자 출력 - 따옴표 없이
print(75)
print(2.3)

# 문자 출력 - 따옴표로 감싸기
print("설비 데이터 배우기")
print('작은 따옴표 가능')

# 여러 값 함께 출력 - 쉼표
# 형식: print(값1, 값2, ...)
# 쉼표로 나누면 한줄 사이에 한 칸 비어짐
print("온도", 75) # 온도 75

print("=== 1번 설비 측정값 ===")
print("온도(℃):", 75)
print("진동(mm/s):", 2.3)

# 계산 결과 출력 - 사칙연산
# 형식: 더하기 + 빼기 - 곱하기 * 나누기 /
print("75 + 5 =", 75 + 5)
print("75 - 5 =", 75 - 5)
print("10 * 3 =", 10 * 3)
print("10 / 3 = ", 10 / 3)

# 주석 - 사람만 읽는 메모
# 형식: # 뒤의 내용은 컴퓨터가 실행하지 않음

print("==== 1번 설비 점검 =====")
print("온도(℃):", 71 + 10) # 정상 온도 71
print("온도 상승량:", 82 - 71) # 상승량

temp = 25
print(temp) # 25 (값)
print("temp") # 이름

# 변수와 할당  - 값에 이름 붙이기
#  형식: 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장"하라는 명령

temp = 25
name = "센서A"
count = 3

print(temp)
print("temp")
x = 10
x = x + 5
print(x)
print(name)
print(count)

# 변수 이름 규칙
# 형식: 영문자,숫자,밑줄 사용 가능 / 숫자로 시작 불가 / 공백도 불가
sensor_count = 3 # sanke_case
temp2 = 10  # 숫자 사용 가능 (숫자로 시작X)
# 2temp = 2 # SyntaxError: invalid syntax (숫자로 시작 불가)

# 대소문자 구분, 재할당
temp = 25
TEMP = 100
print(temp, TEMP)
# 재할당: 마지막에 저장한 값만 남음
score = 10
score = 20
score = 30
print(score) # 30

temp = 25
print(temp)
name = "sensorA"
print(name)

temp = 30 # 30으로 재할당
print(temp)
temp = ("temperature")

my_number = 1
print(my_number)
mood = "행복"
print(mood)

age = 30
label = ("나이")
print(label)
print(age)

print("===========================")

print("실습 5")
x = 10
print(x)
x = x + 5
print(x)
x = x * 2
print(x)

print("실습 6")
a = 100
b = a
a = 999
print(a)
print(b) # b는 a와 다른 변수이므로 값이 바뀌지 않음

print("실습 7")
temper =25
print(temper)
score = 90
print(score)

print("실습 8")
temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 100 
print(temp)

print("실습 9")
x = 5
x = 10
x = x + 1
print(x)

print("실습 10")
name = ("이광호")
temp = 30
name2 = ("포항")
print(name) , print(temp) , print(name2)

print("실습 11")
a , b = 25 , 3
device_temp , sensor_count = a , b
print(device_temp) , print(sensor_count)

print("실습 12")
x , y , z = 10 , 20 , 30
print(x) , print(y) , print(z)
snake , winter = 4 , 3
print(snake) , print(winter)

