# Import Modules
import os
import csv


# Declare/Initialize Variable
datapath = os.path.join('resources', 'ElectionData.csv')
candidates = []
voteCount = []
totalVotes = 0
winner = ''
temp = 0

#Read-in CSV file and sum up votes per candidate
with open(datapath) as csvfile:
    
    dataparser = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(dataparser)

    for row in dataparser:
        
       
        totalVotes += 1
        candidate = row[2]
        
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            voteCount[candidate_index] = voteCount[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            voteCount.append(1)


for i in range(len(candidates)):

    if voteCount[i] > temp:
        temp = voteCount[i]
        winner = candidates[i]
    

# Print output to terminal 
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {totalVotes}")
print(f"----------------------------")

for j in range(len(candidates)):

    print(f"{candidates[j]}: {((voteCount[j]/totalVotes)*100):.2f}% ({voteCount[j]})")

next 

print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")



'''# Output files
output_file = os.path.join("analysis", "ElectionResults.txt")

with open(output_file,"w") as file:
    
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {votesTotal}\n")
    file.write(f"----------------------------\n")
    file.write(f"Khan:     {percentageKhan:.2f}% ({votesKhan})\n")
    file.write(f"Correy:   {percentageCorrey:.2f}% ({votesCorrey})\n")
    file.write(f"Li:       {percentageLi:.2f}% ({votesLi})\n")
    file.write(f"O'Tooley: {percetnageOtooley:.2f}% ({votesOtooley})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"----------------------------")'''