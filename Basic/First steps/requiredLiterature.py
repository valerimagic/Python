bookSheet = int(input())
sheetFor1hour = int(input())
days = int(input())

totalTymeForReading = bookSheet / sheetFor1hour
needHoursForReading = totalTymeForReading / days

print(needHoursForReading)