import math

depositSum = float(input())
months = int(input())
interest = float(input())

result = depositSum + (months * (((depositSum * interest)/100) / 12))

print(result)