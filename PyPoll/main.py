import os
import csv

election_data_csv = os.path.join("./", "election_data.csv")
election_data_result_csv = os.path.join("./", "election_data_result.csv")

total_votes = 0
candidates = {}
votes_per_candidate = []

with open(election_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    for row in csv_reader:
        if row:
            total_votes = total_votes + 1

            try:
                if row[2] in candidates:
                    candidates[row[2]] = candidates[row[2]] + 1
                else:
                    candidates[row[2]] = 1
            except IndexError:
                continue

    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------')

    for candidate in candidates:
        print(f'{candidate}: {(candidates[candidate]/total_votes) * 100:.3f}% ({candidates[candidate]})')

    print('-----------------------')
    print(f'Winner: {max(candidates, key=candidates.get)}')
    print('-----------------------')

csv_file.close()

file = open(election_data_result_csv, "w")
file.write('Election Results\n')
file.write('----------------------\n')
file.write(f'Total Votes: {total_votes}\n')
file.write('----------------------\n')
for candidate in candidates:
    file.write(f'{candidate}: {(candidates[candidate] / total_votes) * 100:.3f}% ({candidates[candidate]})\n')

file.write('-----------------------\n')
file.write(f'Winner: {max(candidates, key=candidates.get)}\n')
file.write('-----------------------\n')
