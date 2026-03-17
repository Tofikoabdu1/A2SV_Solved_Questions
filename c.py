n, s = map(int, input().split())
a = list(map(int, input().split()))
l = 0
curr_sum = 0
tot = 0
for r in range(n):
    curr_sum += a[r]
    while curr_sum > s:
        curr_sum -= a[l]
        l += 1
    tot += (r - l + 1)
print(tot)

