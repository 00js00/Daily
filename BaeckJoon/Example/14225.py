#수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

#2021.03.01 SJW
n = int(input())
s = list(map(int,input().split()))
c = [False] * (n*100000 + 10)
def solve(index, sum):
  if index == n:
    c[sum] = True
    return
  solve(index+1,sum+s[index])
  solve(index+1,sum)
solve(0,0)
i = 1
while True:
  if c[i] == False:
    break
  i += 1
print(i)

#2021.03.01 BJ
'''n = int(input())
a = list(map(int,input().split()))
c = [False] * (n*100000 + 10)

def solve(index,sum):
  if index == n:
    c[sum] = True 
    return
  solve(index+1,sum+a[index])
  solve(index+1,sum)
solve(0,0)
i = 1
while True:
  if c[i] == False:
    break
  i += 1
print(i)'''