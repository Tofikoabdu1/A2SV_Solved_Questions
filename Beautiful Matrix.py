mat = []
for i in range(5):
    x = list(map(int , input().split()))
    mat.append(x)
# print(mat)
x , y = 0 , 0
for row in range(5):
    for col in range(5):
        if mat[row][col] == 1:
            x = row + 1
            y = col + 1
# print(x,y)
print(abs(3-x)+abs(3-y))
