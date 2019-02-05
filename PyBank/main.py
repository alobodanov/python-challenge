import os
import csv

cereal_csv = os.path.join("./", "budget_data.csv")
numberMonth = 0;
netTotal = 0;

with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        if row:
            numberMonth = numberMonth + 1;
            netTotal = netTotal + int(row[1]);

    print('Financial Analysis');
    print('----------------------------');
    print(f'Total Month: {numberMonth - 1}');
    print(f'Total: ${netTotal}');
    print(f'Average Change: {netTotal / (numberMonth - 1)}');
    print(f'Greatest Increase in Profits: {numberMonth - 1}');
    print(f'Greatest Decrease in Profits: {numberMonth - 1}');
