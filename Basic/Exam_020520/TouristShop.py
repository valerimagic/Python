import math
budget = float(input())

number_bought = 0
paid_price = 0
end = True
item = input()
while item != "Stop":

    price = float(input())

    if (number_bought + 1) % 3 == 0:
        price = price / 2
    if budget - price >= 0:

        budget -= price
        paid_price += price
        number_bought += 1
    else:
        print("You don't have enough money!")
        need_money = abs(budget - price)
        print(f"You need {need_money:.2f} leva!")
        end = False
        break
    item = input()

if end == True:
    print(f"You bought {number_bought} products for {paid_price:.2f} leva.")