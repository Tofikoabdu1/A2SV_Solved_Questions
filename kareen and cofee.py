n, k , q = map(int , input().split())
range_ = 200000
temp = [0] * (range_ + 2)
for i in range(n):
    l , r = map(int , input().split())
    temp[l] += 1
    temp[r + 1] -= 1
for i in range(1, range_ + 1):
    temp[i] += temp[i - 1]
for i in range(1, range_ + 1):
    if temp[i] >= k:
        temp[i] = 1
    else:
        temp[i] = 0
for i in range(1, range_ + 1):
    temp[i] += temp[i - 1]
for i in range(q):
    left , right = map(int , input().split())
    print(temp[right] - temp[left - 1])
