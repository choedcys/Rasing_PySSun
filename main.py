width = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
height = ['1', '2', '3', '4', '5', '6', '7', '8']
x = 0
y = 0
count = 0
pos = input("위치 입력: (a~h)(1~8)")

for i in range(0, 8):
    if pos[0] == width[i]:
        x = i
    if pos[1] == height[i]:
        y = i
xt = x
yt = y
for i in range(0, 4):
    if i == 0:
        xt += 2
        if xt <= 7:
            for j in range(0, 2):
                if j == 0:
                    yt += 1
                else:
                    yt -= 2
                if yt <= 7 and yt >= 0:
                    count += 1
    elif i == 1:
        xt -= 2
        if xt >= 0:
            for j in range(0, 2):
                if j == 0:
                    yt += 1
                else:
                    yt -= 2
                if yt <= 7 and yt >= 0:
                    count += 1
    elif i == 2:
        yt += 2
        if yt <= 7:
            for j in range(0, 2):
                if j == 0:
                    xt += 1
                else:
                    xt -= 2
                if xt <= 7 and xt >= 0:
                    count += 1
    else:
        yt -= 2
        if yt >= 0:
            for j in range(0, 2):
                if j == 0:
                    xt += 1
                else:
                    xt -= 2
                if xt <= 7 and xt >= 0:
                    count += 1
    xt = x
    yt = y
print(count)