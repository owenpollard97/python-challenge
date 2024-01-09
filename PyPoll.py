import csv

#CSV Reader
#csvreader = csv.reader(election_data)

#Variable Declaration
candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0

#Open CSV
with open('C:/Users/owenp/OneDrive/Documents/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += 1
        all_candidates.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])

#Votes per Candidate
for b in range(len(candidates)):
    count = 0
    for C in range(len(all_candidates)):
        if candidates[b] == all_candidates[C]:
            count += 1
    data[candidates[b]] = count

#Results Printed
print("Election Results")
print("______\n")
print("Total Votes: %d" % total)
print("______\n")

#Percentages of Votes
for candidate in candidates:
    percentage = (data[candidate] / total) * 100
    percent_list.append(percentage)
    print("%s: %.3f%% (%d)" % (candidate, percentage, data[candidate]))

#Who Won?
print("____________\n")
winner = candidates[percent_list.index(max(percent_list))]
print("Winner: " + winner + "\n")
print("\t_________\n")