sideA = int(input())
sideB = int(input())
sideC = int(input())
occupied = float(input())

volumeAquarium = (sideA * sideB * sideC) * 0.001
occupiedPercent = occupied * 0.01
needWater = volumeAquarium * (1 - occupiedPercent)


print(needWater)