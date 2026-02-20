n = int(input())
arr  = list(map(int , input().split()))
arr.sort()
cnt = 1
train = 0
for i in range(len(arr)):
    if arr[i]>train:
        train+=1
        cnt+=1
print(cnt-1)
