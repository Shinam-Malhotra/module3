file = open("Resources/election_data.csv", "r")
header = file.readline()

candidates = {}

data = file.readlines()

for index in range(len(data)):
    data[index] = data[index].strip('\n')

totalVotes = 0
for candidate in data:
    parts = candidate.split(",")
    if parts[2] not in candidates:
        candidates[parts[2]] = 1
    else:
        candidates[parts[2]] += 1

    totalVotes += 1

winnerVotes = max(list(candidates.values()))
index = list(candidates.values()).index(winnerVotes)
winnerName = list(candidates.keys())[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalVotes)}")
print("--------------------------")
for name, votes in candidates.items():
    percent = votes/totalVotes * 100
    print(f"{name}: {str(round(percent,3))}% ({str(votes)})")

print("--------------------------")
print(f"Winner: {winnerName}")
print("--------------------------")

oFile = open("analysis.txt", "w")
oFile.write("Election Results\n")
oFile.write("--------------------------\n")
oFile.write(f"Total Votes: {str(totalVotes)}\n")
oFile.write("--------------------------\n")

for name, votes in candidates.items():
    percent = votes/totalVotes * 100
    oFile.write(f"{name}: {str(round(percent,3))}% ({str(votes)})\n")

oFile.write("--------------------------\n")
oFile.write(f"Winner: {winnerName}\n")
oFile.write("--------------------------\n")
oFile.close()