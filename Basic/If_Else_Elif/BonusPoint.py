number = int(input())

count = number

if number <= 100:
    count += 5
elif number > 100 and number < 1000:
    count = number * 1.2
elif number > 1000:
    count = number * 1.1

if number % 2 == 0:
    count += 1
if number % 10 == 5:
    count += 2

print(count - number)
print(count)