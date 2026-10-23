# join - 내용을 합치는 역할 (리스트 -> 문자열)
# 형식: '구분자'.join(리스트) (구분자가 앞에 옴)
print('-'.join(['2025','01','15'])) # 2025-01-15

# split + join
# - split: 문자열 -> 리스트
# - join: 리스트 -> 문자열
raw = ('사과','배','감')
p = raw
print('/'.join(p))
print('/'.join([p[0].strip(),p[1].strip(),p[2].strip()]))

print("실습")

print('-'.join(['2025','01','15']))

print('2025','01','15',sep='-')
print('2025','01','15',sep=',')

text = '2025/01/15'
parts = text.split('/')
joined = '-'.join(parts)
print(joined)

raw = "1, NORMAL ,25.3"
parts = raw.split(",")
status = parts[1].strip().lower()
print(status)

# ============================================
# f-string - 문자열 안에 변수 바로 끼우기
# 형식: f"~~~{변수}~~"

name = "홍길동"
age = 25
print(f'{name}님은 {age}살 입니다')

# 숫자도 str 변환 없이 바로 들어감
print(f'온도: {25}')
# 중괄호 안에 계산식 가능
hours = 3
print(f'{hours * 60}분')

# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 둘째 자리까지 (자동 반올림)
value = 25.34567
print(f'측정값: {value:.2f}')
print(f'측정값: {value:.1f}')

print("실습")

name = "PUMP_A"
raw = "87도"
print(f'설비:{name} 현재온도:{raw}')

a = 30
b = 40
c = 70
print(f'세 값의 평균: {(a + b + c)/3}')

value = 87.456
print(f'측정값: {value:.1f}')
print(f'측정값: {value:.2f}')

# 실습 4
raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(',')
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")

# =========================================================
# 리스트 
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

temps = [25, 26, 24, 28, 27] # 숫자 리스트
machines = ["펌프", "모터", "압축기"] 
mixed = ["펌프", 87, True] # 종류가 달라도 한 리스트에 담을 수 있음

print(len(temps)) #5
print(len([])) #0

print("실습")
temps = [17, 32, 34, 32, 19]
print(temps)
print(len(temps))
print(len([]))
print("실습2")
temps = [23, 24, 25, 26, 27, 28]
print(temps[0])
print(temps[2])
print(temps[-1])
# 실습3
line = [10, 15, 20, 25, 30, 35]
print((line[0] + line[-1]) / 2)
# 실습4
temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(temps[0:3],temps[-3:])
print(len(temps[0:3]))
print(len(temps[-3:]))
# 실습5
temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
first = temps[0:6]
second = temps[-6:]
print(first,second)
print(len(first))
print(len(second))

# ================================
# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새로운 값 , 값 in 리스트
nums = [25, 26, 27, 24, 28]
nums[2] = 99
print(nums)

# 값 추가 -append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
data = [25, 26, 24]
data.append(28)
data.insert(1, 99)
data.extend([30,31])
print(data)

# =======================================
print("실습")
data = [21, 22, 23, 240, 25]
data[3] = 24
print(data)

data = []
data.append(30)
print(data)
data.insert(0, 28)
print(data)
temps = [31, 32]
data.extend(temps)
print(data)

# =================================
# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)
print(d)
got = d.pop(1)
print(got, d)
del d[0]
print(d)

# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort() .reverse() .count(값) .index(값)
l = [27, 24, 30, 22, 26]
l.sort()
l.sort(reverse=True)
l.reverse()
print(1)

print("실습")
data = [25, 26, 999, 24, 28, 26]
data.remove(999)
print(data)
remove = data.pop(1)
print(remove)
print(data)
del data[0]
print(data)
print("실습")
data = [22, 23, 25, 22, 21, 26, 20]
data.sort()
print(data)
data.sort(reverse=True)
print(data)
data.reverse()
print(data)
print(data.count(22))
print(data.index(23))
