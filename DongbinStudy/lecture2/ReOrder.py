# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다

n = input()

## n.isalpha()

num = 0
alpha = []

for x in n:
  if x.isalpha():
    alpha.append(x)
  else:
    num += int(x)
alpha.sort()

if num != 0:
  alpha.append(str(num))

print(''.join(alpha))
