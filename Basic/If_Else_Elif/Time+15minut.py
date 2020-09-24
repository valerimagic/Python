hour = int(input())
minuts = int(input())

if (minuts + 15) >= 60:
    hour += 1
    minuts = minuts + 15 - 60
else:
    minuts += 15
if hour > 23:
    hour = hour - 24

if minuts < 10:
    print(f"{hour}:0{minuts}")

else:
    print(f"{hour}:{minuts}")
