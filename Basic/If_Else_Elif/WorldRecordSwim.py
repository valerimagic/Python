import math

record = float(input())
distance = float(input())
timeForMeter = float(input())

needTime = distance * timeForMeter
resistanceTime = math.floor(distance / 15) * 12.5

totalTime = needTime + resistanceTime
deficitTime = totalTime - record

if record <= totalTime:
    print(f"No, he failed! He was {deficitTime:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")
