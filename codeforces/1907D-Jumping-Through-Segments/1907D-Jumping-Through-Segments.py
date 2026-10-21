def can(k):
  left = 0
  right =0
  for l,r in seg:
    left = max(left - k , l)
    right = min(right + k , r)
    if left > right:
      return False
  return True
for i in range(t):
  n = int(input())
  seg = []
  for i in range(n):
    x = list(map(int , input().split()))
    seg.append(x)
  l = 0
  r = 10**9
  while l < r:
    mid = (l+r)//2
    if can(mid):
      r = mid
    else:
      l = mid+1
  print(l)



  # print(seg)