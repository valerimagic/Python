import math

number = float(input())
firstUnit = input()
secondUnit = input()

if firstUnit == "mm" and secondUnit == "m":
    print(F"{(number / 1000):.3f}")
elif firstUnit == "mm" and secondUnit == "cm":
    print(F"{(number / 10):.3f}")
elif firstUnit == "cm" and secondUnit == "m":
    print(F"{(number / 100):.3f}")
elif firstUnit == "cm" and secondUnit == "mm":
    print(F"{(number * 10):.3f}")
elif firstUnit == "m" and secondUnit == "cm":
    print(F"{(number * 100):.3f}")
elif firstUnit == "m" and secondUnit == "mm":
    print(F"{(number * 1000):.3f}")