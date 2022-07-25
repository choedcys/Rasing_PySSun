x = int(input("시간입력: "))
sec = 3600*x + 59*60 +59
count = 0
for i in range(0, sec+1):
    temp = i
    h = temp // 3600
    temp -= h*3600
    m = temp //60
    temp -= m*60
    if h % 10 == 3 or h//10 == 3 or m % 10 == 3 or m//10 == 3 or temp % 10 == 3 or temp//10 == 3:
        print(h,"시 ",m,"분 ", temp,"초")
        count += 1
print(count)