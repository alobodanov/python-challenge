import os
import csv

budget_data_csv = os.path.join("./", "budget_data.csv")
budget_data_result_csv = os.path.join("./", "budget_data_result.csv")

month_total = 0
month_change = []
data = []
net_total = 0
average_profit = 0
original_profit = 0
greatest_value = 0
greatest_date_on = 0
lowest_value = 0
lowest_date_on = 0

with open(budget_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    for row in csv_reader:
        if row:
            data.append(row[0])
            month_total = month_total + 1
            net_total = net_total + int(row[1])

            original_profit = int(row[1])
            change_profit = original_profit - average_profit
            average_profit = original_profit

            month_change.append(original_profit)

            greatest_value = max(month_change)
            lowest_value = min(month_change)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Month: {month_total}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${( int(greatest_value) - int(lowest_value )) / int(month_total) - 2}')
    print(f'Greatest Increase in Profits: {data[month_change.index(greatest_value)]} (${greatest_value})')
    print(f'Greatest Decrease in Profits: {data[month_change.index(lowest_value)]} (${lowest_value})')

csv_file.close()

file = open(budget_data_result_csv, "w")
file.write('Financial Analysis\n')
file.write('----------------------------\n')
file.write(f'Total Month: {month_total}\n')
file.write(f'Total: ${net_total}\n')
file.write(f'Average Change: ${( int(greatest_value) - int(lowest_value )) / int(month_total) - 2}\n')
file.write(f'Greatest Increase in Profits: {data[month_change.index(greatest_value)]} (${greatest_value})\n')
file.write(f'Greatest Decrease in Profits: {data[month_change.index(lowest_value)]} (${lowest_value})\n')
file.close()
