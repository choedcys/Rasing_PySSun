destin=[]
i = 0
pathx = 1
pathy = 1
width = int(input("가로 좌표: "))
height = int(input("세로 좌표: "))

while 1:
    temp = input("오른쪽:R 왼쪽:L 위:U 아래:D 종료:0")
    if temp == '0':
        break
    destin.append(temp)
    i = i+1

for i in range(0,len(destin)):
    if destin[i] == 'R':
        if pathx%width != height:
            pathx=pathx+1
    elif destin[i] == 'L':
        if pathx % width != 0:
            pathx = pathx - 1
    elif destin[i] == 'U':
        if pathy > 1:
            pathy=pathy-1
    else:
        if(pathy <= height-2):
            pathy=pathy+1
print("시작: (1, 1)")
print("위치: (",pathx,", ",pathy,")")