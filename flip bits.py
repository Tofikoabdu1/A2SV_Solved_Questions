t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    balance = [0] * n
    cnt0 = cnt1 = 0
    
    for i in range(n):
        if a[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        if cnt0 == cnt1:
            balance[i] = 1
    flip = 0
    flag = True
    for i in range(n - 1, -1, -1):
        cur = a[i]
        if flip % 2 == 1:
            if cur == '0':
                cur = '1'
            else:
                cur = '0'
        if cur != b[i]:
            if balance[i] == 0:
                flag = False
                break
            flip += 1
    
    print("YES" if flag else "NO")
