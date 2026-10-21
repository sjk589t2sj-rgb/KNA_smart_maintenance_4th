# 자료형 

count = 3    # int 정수
temp = 25.5  # float 실수
name = "센서A"  # str 문자열

ok = True  # bool 불린형
no = False  # bool 불린형

#  type() 함수는 자료형을 확인할 수 있다.
print(type(25))            # <class 'int'>
print(type("센서A"))       # <class 'str'>
print(type(ok))            # <class 'bool'>

# 자료형마다 다른 동작
print(3 + 5)
print("3" + "5") # 문자열 연결

print("=======================================")

print("실습1")
count = 3
temp = 25.5
name = "센서A"
is_ok = True

print("실습2")
print(type(3))
print(type(25.5))
print(type("센서A"))
print(type(is_ok))

print("실습3")
print(type(100))  # int
print(type(100.0)) # float
print(type("100")) # str

print("실습4")
print(3 + 5)
print("3" + "5")
print("악어" + "기린")

print("실습5")
print(3 > 2) # True
print(5 == 5) # False

print("실습6")
# print(type(10.1 + "악어")) # 재할당
print(type(10.1 + 0.2))
print(type("악어 + 기린"))

print("실습7")
device_temp = 25.5
check_count = 3
device_name = ("센서A")
is_normal = 2

print("===========================================")

# 연산자
# 산술, 비교, 논리 연산자

# 산술 연산자
# 형식: +,-,*,/,//(몫),%(나머지),**(거듭제곱)

# 우선순위
# 곱셈,나눗셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식: score += 10 <-> score = score + 10 더 짧게 쓰기위해 쓰는 기호
score = 100
score += 10
print(score) # 110이 나오게 됨
# -=, *=, /= 사용도 가능

# 문자열 연산
# +,* 가능
print("안녕" + "하세요") #안녕하세요
print("-" * 4) # ---- 
# 주의) 자료형이 같은 것끼리 연산 가능

print("실습1")
a = 17
b = 5
print(a + b , a - b , a * b , a / b , a // b , a % b , a ** b )

print("실습2")
c = 3
d = 4
e = 5
print((c + d + e) / 3 )
print((c + d + e) ** 2)
print(3 * 3 * 3)

# 비교 연산자
# 형식: == (같다) , != (다르다) , < > , <= >=
print(5 == 5) # True
print("정상" == "정상") # True
print("A" == "a") # False

# 논리 연산자
# - and: 모두 참이어야, or: 하나만 참이어도 참, not: 반대
print(True and False) #False
print(True or False) #True
print(not True) #False

print("실습3")
print(5 == 5)
print(5 >= 5)
print(5 > 3)
print(3 < 5)
print(5 <= 5)
print(5 != 3)

print("실습4")
temp = 85
print(temp > 60 and temp < 90)
temp1 = 5
print(temp1 > 3 and temp1 < 7)

print("실습5")
score = 100
score += 50
score -= 30
score += 5
print(score)

print("실습6")
score = 500
score -= 23
print(score * 0.01) # 4.7%
score = 21
print((score / 24) * 100) #87.5%

print("실습7")
score = 500
print(score / 60) # 약 8시간 30분

# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input("안내문구: ")
name = input("이름: ")
age = input("나이: ")
print(name)

# 형변환 - int(정수), float(실수), str(문자)
# print(age + 1) #typeerror
print(int(age) + 1) # int() 형변환

print("실습")
age = int(input("태어난 해:"))
print("당신의 나이는 만",(2026-age), "세 입니다")

height = float("173.5") # float() 실수 변환
print(height, type(height))

print("실습2")
city = input("거주 국가: ")
city1 = input("거주 도시: ")
print(city ,"의" , city1,"에서 거주하시는군요.")

print("실습3")
name = input("성함: ")
city = input("도시: ")
print("당신의 이름", name,"당신의 사는 곳은", city)

print("실습4")
a = int(input("숫자: "))
b = int(input("숫자: "))
print("두 숫자의 합은", a + b)
print("두 숫자의 곱은", a * b)

print("실습5")
a = int(input("현재 온도: "))
print("기준온도(50도) 초과", a > 50)
print("기준온도(50도) 미만", a < 50)

print("실습6")
a = int(input("국어점수: "))
b = int(input("수학점수: "))
c = int(input("영어점수: "))
abc = (a + b + c) / 3
print("70점 이상 합격", abc >= 70)


# =========================================
# 문자열
# -"", '', 감싸서 표현

# 여러줄 문자열
# 형식: 삼중 따옴표 """ 적을 내용.."""
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(notice)

# 이스케이프 : \n 줄바꿈, \t 탭
print("이름\t상태")
print("첫줄\n둘째 줄")

print("실습1")
notice = """ 가동 점검표
/ 1. 온도 확인
/ 2. 압력 확인"""
print(notice)

print("실습2")
# 설비코드, 상태, 날짜를 조합해 하나의 라벨 문자열

name = ("PUMP_A")
status = ("정상")
code = ("2025-01-15")
print(name,"/"+status,"/"+code)

print("실습3")
# 코드 상태 가동시간(int) 점검일
hours = 1200


