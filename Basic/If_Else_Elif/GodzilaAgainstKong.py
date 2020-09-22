import math

budgetFilm = float(input())
statisCount = int(input())
priceForOneStatist = float(input())

sumForDecor = budgetFilm * 0.1
sumForDress = statisCount * priceForOneStatist
if statisCount > 150:
    sumForDress = sumForDress - (sumForDress * 0.1)
totalSumForFilm = sumForDecor + sumForDress
balance = budgetFilm - totalSumForFilm

if balance < 0:

    balance = math.fabs(balance)
    print("Not enough money!")
    print(f"Wingard needs {balance:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {balance:.2f} leva left.")