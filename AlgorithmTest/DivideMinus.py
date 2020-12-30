## ~ing  20201229 SJW

<<<<<<< HEAD
## 1이 될 때 까지

n, k = map(int, input().split())
rerult = 0

## SJW
while n > 1:
	if n % k == 0:
		n /= k
		result += 1
	else:
		n -= 1
		result += 1

print(result)

##### 답안 예시
## 시간복잡도를 줄여 빠르게 해결할 수 있다

while True:
	# N이 K로 나누어 떨어지는 수가 될 때까지 빼기
	target = (n // k) * k
	result += (n - target)
	n = target
	# N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
	if n < k:
		break
	# K로 나누기
	result += (n - 1)
	print(rerult)
=======
n = 7
k = 3

while n == 1:
  if n %= 0 :
    n /= k
    print(n)
  else:
    n =- 1
    print(n)
print(n,k)
>>>>>>> bb50afe2e6d294f2d62dcedce6c8bec09a920ddf
