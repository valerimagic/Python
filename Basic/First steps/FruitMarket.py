berries = float(input())
bannana = float(input())
orange = float(input())
raspberries = float(input())
berriesPerKG = float(input())

priceRaspberries = berries / 2
priceOranges = priceRaspberries - (0.4 * priceRaspberries)
priceBannana = priceRaspberries - (0.8 * priceRaspberries)
sumRaspberries = raspberries * priceRaspberries
sumOranges = orange * priceOranges
sumBannanas = bannana * priceBannana
sumBerries = berriesPerKG * berries

totalSum = sumRaspberries + sumOranges + sumBannanas + sumBerries

print(totalSum)
