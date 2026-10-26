# 조건문
#  if 기본 구조 - 콜론과 들여쓰기 (코드 블록)
# 형식: 
# if 조건식 : 
#  실행할 코드 (들여쓰기)
# temp = 85
# if temp > 80:               # 콜론: 블록 시작 신호
    # print("온도 주의")       # 들여쓰기 안 -> 조건 참일 때만 실행
    # print("점검 요망")
# print("측정 종료")           # 들여쓰기 끝 -> 조건과 무관하게 항상 실행

# else - 조건이 거짓일 때
# 형식: 
# if 조건문:
#   참일 때 코드
# else:
#   거짓일 때 코드
score = 55
# if score >= 60:
    # print("합격")
# else:
    # print("불합격")

# print("실습")
# score = int(input("나이를 입력 하세요."))
# if score > 18:
    # print("성인입니다")
# else:
    # print("미성년자입니다")

# elif
# 형식: 
# if .. elif ... else (위에서부터 검사, 처으 참인 곳만 실행)

score = 82
# if score >= 90:
    # print("우수")
# elif score >= 70:
    # print("보통")
# else:
    # print("미흡")

# print("실습")

# score = int(input("점수를 입력하세요."))
# if score >= 90:
    # print("수")
# elif score >= 80:
    # print("우")
# elif score >= 70:
    # print("미")
# else:
    # print("양")

# 논리 연산자 and or not / 범위 조건
temp = 45
# print(temp >= 20 and temp <= 60)

# if 20 <= temp <= 60:
    # print("정상범위")

# print("실습")
# score = int(input("측정 온도를 입력하세요."))
# if score <= 50:
    # print("정상")
# elif score > 80:
    # print("위험")
# elif score > 60:
    # print("주의")
# else:
    # print("error")

# a = input("아이디를 입력하세요.")
# b = input("비밀번호를 입력하세요.")
# a1 = ("이광호")
# b1 = ("1234")
# if a1 == a and b1 == b:
#     print("로그인 성공")
# else:
#     print("로그인 실패")

# # 실습 5 : 중첩 if
# temp = int(input("온도: "))
# vib = float(input("진동: "))
# current = int(input("전류: "))

# if temp > 80 or vib > 4.0:
#     print("위험: 즉시 정지")
# else:
#     if current > 60 and temp > 70:
#         print("주의: 부하 점검")
#     elif vib > 2.5:
#         print("주의: 진동 관찰")
#     else:
#         print("정상")

# # for 반복문
# # for문 (range 이용한 반복)
# # 형식: for 변수 in range(횟수):
# for i in range(5):
#     print("안녕하세요")

# for i in range(5):
#     print(i)

# # range (시작, 끝, 증가값)
# for i in range(1, 10, 2):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# print("실습")

# for i in range(1,6):
#     print(i)
# for i in range(2,6,2):
#     print(i)
# for i in range(5, 0, -1):
#     print(i)

# 누적 변수 패턴 (합계, 갯수, 평균)
total = 0
for i in range(1,6):
    total += i
print("합계:", total)

# 조건 만족하는 경우 세기
count = 0
for i in range(1, 11):
    if i > 5:
        count += 1
print("개수:", count)

# 평균
total, count = 0, 0
for i in range(1, 6):
    total += i
    count += 1
if count > 0:
    print("평균:", total/count)

print("실습")
data = 0
data = int(input("숫자 입력"))

for i in range(1, data):
    data += i
print("합계: ", data)

# enumertate : 순서 + 값을 함께 준다
temps = [25, 26, 24]
for idx, t in enumerate(temps):
    print(idx + 1, "번째: ", t) # 1 번째: 25...

#  중첩 반복 (바깥 한 바퀴마다 안쪽이 처음부터 끝까지)
for dan in range(2, 4):
    for su in range(1, 4):
        print(f'{dan} x {su} = {dan * su}')
    print("------")

print("실습")
for dan in range(2, 10):
    for su in range(1, 10):
        print(f'{dan} x {su} = {dan * su}')
    print("----------")

n = int(input("측정 횟수: "))
over_count = 0
for i in range(n):
    value = int(input("측정값: "))
    if value > 80:
        over_count += 1

print("초과 갯수: " , over_count)

# while - 조건이 참인 동안 반복
# 형식:
# while 조건식:         (조건이 거짓이 되는 순간 멈춤)
# for - '몇 번'이 정해졌을 때, while은 '언제 끝날지 모르지만 조건으로 멈출 때' 사용

count = 1
while count <= 3:
    print(count)
    count += 1
# 주의) 무한루프를 막으려면 (1)언제가 거짓이 될 조건, (2)반복문 안에서 그 조건을 갱신
# 처음부터 조건이 거짓이면 한 번도 실행되지 않는다.

print("실습")
answer = 7
guess = 0
while guess != answer:
    guess = int(input("5 + 2는?: "))
print("정답")