t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    cur = 0
    max1 = 0
    for x in arr1:
        cur += x
        max1 = max(max1, cur)
    cur = 0
    max2 = 0
    for x in arr2:
        cur += x
        max2 = max(max2, cur)
    
    print(max1 + max2)
