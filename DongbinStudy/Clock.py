# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다 00시 00분 03초 , 00시 13분 30초

#SJW
n = int(input())
count = 0

# 1시간 loof

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) +str(j) + str(k):
        count+= 1

print(count)