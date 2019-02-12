import os
import csv


class Budget:

    def __init__(self):
        self.total_month = []
        self.total_change = []
        self.monthly_change = []
        self.budget_data_csv = os.path.join('./', 'budget_data.csv')
        self.budget_data_result_csv = os.path.join('./', 'budget_data_result.txt')

    def open_file(self):
        with open(self.budget_data_csv, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            self.read_data(csv_reader)

    def read_data(self, reader):
        for row in reader:
            self.total_month.append(row[0])
            self.total_change.append(int(row[1]))

        self.average_change()

    def average_change(self):
        for i in range(len(self.total_change) - 1):
            self.monthly_change.append(self.total_change[i + 1] - self.total_change[i])

    def terminal_output(self):
        print('Financial Analysis')
        print('----------------------------')
        print(f'Total Month: {len(self.total_month)}')
        print(f'Total: ${sum(self.total_change)}')
        print(f'Average Change: ${sum(self.monthly_change) / len(self.monthly_change):.2f}')
        print(f'Greatest Increase in Profits: '
              f'{self.total_month[self.monthly_change.index(max(self.monthly_change)) + 1]} '
              f'(${max(self.monthly_change)})')
        print(f'Greatest Decrease in Profits: '
              f'{self.total_month[self.monthly_change.index(min(self.monthly_change)) + 1]} '
              f'(${min(self.monthly_change)})')

    def file_output(self):
        with open(self.budget_data_result_csv, 'w') as file:
            file.write('Financial Analysis\n')
            file.write('----------------------------\n')
            file.write(f'Total Month: {len(self.total_month)}\n')
            file.write(f'Total: ${sum(self.total_change)}\n')
            file.write(f'Average Change: ${sum(self.monthly_change) / len(self.monthly_change):.2f}\n')
            file.write(f'Greatest Increase in Profits: '
                       f'{self.total_month[self.monthly_change.index(max(self.monthly_change)) + 1]} '
                       f'(${max(self.monthly_change)})\n')
            file.write(f'Greatest Decrease in Profits: '
                       f'{self.total_month[self.monthly_change.index(min(self.monthly_change)) + 1]} '
                       f'(${min(self.monthly_change)})\n')


Budget = Budget()
Budget.open_file()
Budget.terminal_output()
Budget.file_output()
