## 팩토리얼 구현
## n! = 1 x 2 x 3 x ... x (n-1) x n

## def 구현
## 반복 사용
def factorial_iterative(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

# 재귀 사용
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))
