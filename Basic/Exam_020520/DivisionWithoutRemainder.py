number_total = int(input())

dve = 0
tri = 0
four = 0

for number in range(1, number_total + 1):
    command = int(input())
    if command % 2 == 0:
        dve += 1
    if command % 3 == 0:
        tri += 1
    if command % 4 == 0:
        four += 1

print(f"{(dve / number_total) * 100:.2f}%")
print(f"{(tri / number_total) * 100:.2f}%")
print(f"{(four / number_total) * 100:.2f}%")
