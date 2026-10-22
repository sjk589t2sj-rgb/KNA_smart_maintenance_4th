# 형식: 문자열[번호]

word = 'PYTHON'
print(word[0], word[2], word[5]) # P T N
#  인덱스: 뒤에서부터 -1, -2

print("실습")
word = 'SIGNAL'
print(word[-1], word[-2])

print("실습")
word = 'SIGNAL'
print(word[0], word[2], word[5])

# 슬라이싱 - 구간으로 잘라내기
# 형식: 문자열[시작:끝] (시작 포함, 끝 제외)
print(word[1:4])

print("실습")
word = 'SIGNAL'
print(word[0:3],word[2:5])

word = 'temp_sensor'
print(word[:4])
print(word[5:])

word = 'sensor_01'
print(word[-2:])

# index
# 주의) 위치를 반환하지만 없으면 오류

print("실습")
fname = "sensor_log.csv"
print(fname.startswith("sensor"))   #True
print(fname.endswith("csv")) #True

print("실습")
label = "WARNING"
print(label == "WARNING")
print(label == "warning")

# ==========================================
#  메서드 - 점(.) 문법
#  형식: 문자열.메서드이름() (--> 꼭 괄호를 붙여야 실행)
# upper() : 모두 대문자 / lower() : 모두 소문자
# word = 'python'
print(word.upper()) #대문자로 바꿔줌
print(word.count('p')) # 1
print(word) # 원본 그대로

print('NORMAL'.lower())
print('python is'.capitalize())
print('hong gil'.title())

print("실습")
word = 'ready'
print(word.upper())

print("실습")
word = 'WARNING'
print(word.lower())

print("실습")
name = 'lee gwang ho'
print(name.title())

print("실습")
a = "Fault"
b = "FAULT"
print(a == b)
print(a.lower() == b.lower())

# 확인 메서드 : is*** 메서드는 참/거짓 반환
print('ABC'.isupper(), 'abc'.islower()) # True

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
raw = ' 정상 '
print('['+ raw + ']')               #[   정상  ]
print('[' + raw.strip() + ']')      #[정상]

print("실습")
print('ABC'.isupper(), 'abc'.islower(), 'Abc'.isupper(), 'Abc'.islower())


print("실습")
fname = "Sensor_LOG.CSV"
low = fname. lower()
print(low.startswith("sensor"))
print(low.endswith(".csv"))
print(fname.endswith(".scv"))

print("실습")
S = " 가동중 "
clean = S.strip()
print("["+ clean +"]")

print("실습")
s = " 대기 "
print("[" + s.lstrip() + "]")
print("[" + s.rstrip() + "]")

print("실습")
s= "***경고***"
print(s.strip("*"))

print("실습")
code = "WARNING"
print(code.strip().lower())

print("실습")
s = " 경보 "
print("[" + s + "]")
s = s.strip()
print("[" + s + "]")

# replace - 바꾸기/지우기
# 형식: 문자열.replace('바꿀것', '새것')
# - 모두 바꾸기, 결과 저장 필요

print('정 상 가 동'.replace(' ',''))
print('010-1234-5678'.replace('-',''))
print('3,000'.replace(',',''))
# 체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 변경

# split - 구분자로 나누기 (결과 -> 리스트)
# 형식: 문자열.split('구분자') (구분자 생략 = 공백 기준)
print('A1 A2 A3'.split())
print('사과,배,감'.split(','))

print("실습")
print('설비 정상 가동'.replace('정상','점검'))

print('PUMP A 03'.split())

print('a,b,c,d'.split(','))

print('a,b,c,d'.split(',',1))