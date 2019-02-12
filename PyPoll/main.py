import os
import csv


class Election:

    def __init__(self):
        self.election_data_csv = os.path.join('./', 'election_data.csv')
        self.election_data_result_csv = os.path.join('./', 'election_data_result.txt')
        self.total_votes = 0
        self.candidates = {}
        self.votes_per_candidate = []

    def open_file(self):
        with open(self.election_data_csv, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            self.create_candidates_dictionary(csv_reader)

    def create_candidates_dictionary(self, reader):
        for row in reader:
            if row:
                self.total_votes = self.total_votes + 1
                try:
                    if row[2] in self.candidates:
                        self.candidates[row[2]] = self.candidates[row[2]] + 1
                    else:
                        self.candidates[row[2]] = 1
                except IndexError:
                    continue

    def terminal_output(self):
        print('Election Results')
        print('----------------------')
        print(f'Total Votes: {self.total_votes}')
        print('----------------------')

        for candidate in self.candidates:
            print(f'{candidate}: {(self.candidates[candidate]/self.total_votes) * 100:.3f}% '
                  f'({self.candidates[candidate]})')

        print('-----------------------')
        print(f'Winner: {max(self.candidates, key=self.candidates.get)}')
        print('-----------------------')

    def file_output(self):
        with open(self.election_data_result_csv, 'w') as file:
            file.write('Election Results\n')
            file.write('----------------------\n')
            file.write(f'Total Votes: {self.total_votes}\n')
            file.write('----------------------\n')

            for candidate in self.candidates:
                file.write(f'{candidate}: {(self.candidates[candidate] / self.total_votes) * 100:.3f}% '
                           f'({self.candidates[candidate]})\n')

            file.write('-----------------------\n')
            file.write(f'Winner: {max(self.candidates, key=self.candidates.get)}\n')
            file.write('-----------------------\n')


Election = Election()
Election.open_file()
Election.terminal_output()
Election.file_output()
