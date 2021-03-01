# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 2021.03.01 SJW
n,m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0

def solve(index,sum):
  global cnt
  if index == n:
    if  sum == m:
      cnt += 1
    return
  solve(index+1,sum+a[index])
  solve(index+1,sum)
solve(0,0)
if m == 0:
  cnt -=1
print(cnt)


# 2021.03.01 BJ
'''n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
def solve(index,sum):
  global ans
  if index == n:
    if sum == m:
      ans += 1
    return
  solve(index+1, sum + a[index])
  solve(index+1, sum)
solve(0,0)
if m == 0:
  ans -=1
print(ans)'''