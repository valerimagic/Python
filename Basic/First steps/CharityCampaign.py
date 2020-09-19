days = int(input())
cakeMaster = int(input())
cakeCount = int(input())
wafflesCount = int(input())
pancake = int(input())

cakePrice = 45
wafflesPrice = 5.8
pancakePrice = 3.2

cake = cakeCount * cakePrice
waffles = wafflesCount * wafflesPrice
pancakeForDay = pancake * pancakePrice

sumForDay = (cake + waffles + pancakeForDay) * cakeMaster
totalSumPerCampany = sumForDay * days
clearSum = totalSumPerCampany - ( totalSumPerCampany / 8)

print(clearSum)
