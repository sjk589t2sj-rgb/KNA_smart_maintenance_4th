# # break - 반복 도중에 완전히 멈추기
# for i in range(1, 11):
#     if i == 5:
#         print(i, "break")
#         break       # 5를 만나면 반복 즉시 종료
#     print(i)

# for i in range(1, 7):
#     if i % 2 == 0:
#         continue
#     print(i)        # 1 3 5

# print("실습")
# data = False
# for v in [62, 78, 92, 65, 70]:
#     if v > 80:
#         data = True
#         print(v, "break")
#         break
# if data: print("발견")
# else: print("없음")

# print("실습")
# data = [26, 27, 28, 30, 31, 32]
# for t in data:
#     if t >= 30:
#         print(t, "고온")
#     else:
#         print(t, "저온")

# data = [5, 2, 4, 12, 9, 10]
# for i in data:
#     if i >= 5 and i <= 10:
#         print(i)

# 최대, 최소
# temp = [25, 32, 28, 36, 27, 31]
# biggest = temp[0]
# for t in temp:
#     if t < biggest:
#         biggest = t    #더 큰값일 때 갱신
# print(biggest)

# #  빈 리스트 채우기
# doubled = []
# for t in temp:
#     doubled.append(t * 2)
# print(doubled)

# print("실습")
# data = [26, 29, 30, 31, 35]
# total = 0
# count = 0
# for t in data:
#     if t > 30:
#         total += t
#         count += 1
# print("고온 평균:", total/count)


# data1 = [22, 23, 32, 35, 31, 33]
# temp2 = []
# for t in data1:
#     if t > 30:
#         print(t)
#         temp2.append(t)
# print(len(temp2), "개"), print(temp2)

# temps = [25, 26, 24, 28, 27]
# data2 = []
# for t in temps:
#     data2.append(t * 1.8 + 32)
# print(data2)


# # 중첩 리스트 -리스트 안에 리스트
# # -표(행,열)처럼 한 줄에 여러 값이 묶인 데이터.
# # 바깥 반복은 '행', 안쪽 인덱스로
# rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# for row in rows:
#     print(row[0], "온도", row[1]) 

# print("실습")
# temp = [25, 27, 31, 35]
# temp2 = []
# total = 0
# count = 0
# for t in temp:
#     total += t
#     count += 1
# print("전체 평균", total/count)
# for t in temp:
#     if t > 30:
#         temp2.append(t)
# print("고온 개수: ",(len(temp2)))
# for t in temp2:
#     total += t
#     count += 1
# print("고온 평균", total/count)

# # 튜플
# # 형식: (값1, 값2, 값3 .....)
# # - 좌표, (이름, 값) 처럼 짝지어진 값을 하나로 묶을 때 사용
# sensor = ("모터 온도", 78)
# print(sensor)
# one = (78,)         # 값이 한개라도 ',' 표시해야 튜플로 인지
# not_tuple = (78)
# print(type(one), type(not_tuple))

# # 튜플 인덱싱, 슬라이싱
# s = ("모터 온도", 78, "C")
# print(s[0], s[-1])
# readings = (78, 80, 79, 95, 77)
# print(readings[1:4])

# # 튜플 언패킹 - 한 번에 변수로 분리
# # 형식: 변수1, 변수2 = 튜플     (변수 개수가 튜플 값 개수와 일치)
# name, value = sensor
# print(name, value)

# sensor = ('모터 온도', 78)
# print(sensor[0])
# print(sensor[1])
# name, temp = sensor
# print(name, temp)

# # 튜플 리스트 + 반복문(언패킹)
# # - (이름, 값) 튜플들을 리스트로 모아 for 순회하면 이름, 값이 자동 분리
# sensors = [("모터 온도", 78), ("펌프 압력", 95)]
# for name, value in sensors:
#     #print(s)
#     if value > 90:
#         print(name, "경고")

# print("실습")
# sensor = [("회전 속도", 78), ("펌프 압력", 95)]
# for name, value in sensor:
#     print(name, value)
#     if value > 90:
#         print(name,"경고")

# # 중첩 튜플
# sensors = ("모터온도", 78, (3,5))
# print(sensors[2][0])

# # 튜플 리스트 정렬
# sensors = [(78, "모터온도"),(95, "베어링진동"),(32, "펌프압력")]
# hot = sorted(sensors, reverse=True)
# print(hot)

print("실습")
sensors = [("모터온도", 78, (3, 5)),
           ("베어링진동", 0.5, (7, 2)),
           ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치: ",x ,y)
    if x <= 5:
        print(name)