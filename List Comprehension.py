if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    # li =[nums for nums in [[i,j,k] for i in range(x) for j in range(y) for k in range(z)] if sum(nums) != n]
    l2 =[num for num in l if sum(num)!=n]
    print(l2)
