# ----------------------------------------------------------------------
# [실습1] 'Hello World' 100번 출력
# ----------------------------------------------------------------------
# 반복문 => for in 반복문 ================================================
# - 여러 개의 데이터를 가지고 있는 데이터에서 한 개 씩 원소/요소를
#   읽어와줌
# for 요소저장변수명 in 여러개 데이터 가진 타입:
# <---->요소/원소 반복할 코드
# <---->요소/원소 반복할 코드
# ----------------------------------------------------------------------
msg="Happy New Year 2024! Good Luck^^"

# msg를 구성하는 문자 한개씩 화면에 한 줄에 한 개씩 출력해주세요!
print(msg[0]) # H
print(msg[1])# a
print(msg[2])# p
print(msg[3])# p
print(msg[4])# y
print(msg[5])#
print(msg[6])# N
print(msg[7])# e

for ele in msg:
    print(ele)

# [실습1] 'Hello World' 100번 출력
for cnt in range(100):
    print("Hello World")

# [실습2] 좋아하는 음식명을 리스트에 저장하기(단, 10개)
foods = ['자장면', '돈까스', '족발', '햄버거', '백반',
         '피자', '소고기', '짬뽕', '라면', '비빔면']

for food in foods: print(food, end=' ')