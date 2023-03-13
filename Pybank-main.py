
file = open("Resources/budget_data.csv", "r")
header = file.readline()
firs_row = file.readline()
data = file.readlines()
total_value = int(firs_row.split(",")[1])

for index in range(len(data)):
    data[index] = data[index].strip('\n')

totalMonths = 1
total = int(firs_row.split(",")[1])
averageChange = 0
total_change = 0

greatestIncreaseMonth = ''
greatestIncreaseProfit = int(data[0].split(',')[1]) - total_value

greatestDecreaseMonth = ''
greatestDecreaseProfit = int(data[0].split(',')[1]) - total_value

for line in data:
    parts = line.split(",")
    month = parts[0]
    profit = int(parts[1])

    totalMonths += 1
    total += profit

    change = profit - total_value
    total_change += change
    total_value = profit

    if change > greatestIncreaseProfit:
        greatestIncreaseMonth = month
        greatestIncreaseProfit = change

    if change < greatestDecreaseProfit:
        greatestDecreaseMonth = month
        greatestDecreaseProfit = change

averageChange = total_change / (totalMonths-1)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str(round(averageChange,2))}")
print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${str(greatestIncreaseProfit)})")
print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${str(greatestDecreaseProfit)})")

oFile = open("analysis.txt", "w")
oFile.write("Financial Analysis\n")
oFile.write("---------------------\n")
oFile.write(f"Total Months: {str(totalMonths)}\n")
oFile.write(f"Total: ${str(total)}\n")
oFile.write(f"Average Change: ${str(round(averageChange,2))}\n")
oFile.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${str(greatestIncreaseProfit)})\n")
oFile.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${str(greatestDecreaseProfit)})\n")

oFile.close()