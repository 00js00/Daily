# 행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면입니다 완실 정원의 특정한 한 칸에 나이트가 서있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다. 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다. 
# 나이트는 특정위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
## 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
## 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
#  나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력

## NDB
input_data = input()
row = int(input_data[1])

## ord : 현재 문자의 유니코드 위치 
col = int(ord(input_data[0])-ord('a'))+1
print(row,col)

type = [(2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)]

result = 0

for i in type:
  col_next = col + i[1]
  row_next = row + i[0]
  
  if col_next >=1 and col_next <=8 and row_next >=1 and row_next <=8:
    result += 1

print(result)
