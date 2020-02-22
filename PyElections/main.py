#import the libraries
import os
import csv

#extract the file path
file_path = os.path.join('.','houston_election_data.csv')
#open file to output the results
elec_result = open("Houston_Election_Results.txt","w")

#initialize the dictionary
candidates={}

#initialize the total number of voters
voterNum = 0

#open the csv file
with open(file_path,'r') as csv_file:

    #read the csv file and assign the content to the variable
    csv_reader = csv.reader(csv_file,delimiter=',')

    #remove the headers
    next(csv_reader)

    #count the number of voters for each candidate and save it to the dictionary
    for row in csv_reader:
        voterNum +=1

        if row[0] in candidates:
            candidates[row[0]] += 1
        else:
            candidates[row[0]] = 1

#print the results to the terminal for each candidate
print("\nHouston Mayoral Election Results")
print("---------------------------------------\n")
print("Total Cast Votes: {}\n" .format(voterNum))
print("---------------------------------------")

print("Houston Mayoral Election Results",file=elec_result)
print("---------------------------------------\n",file=elec_result)
print("Total Cast Votes: {}\n" .format(voterNum),file=elec_result)
print("---------------------------------------",file=elec_result)

#find the max and the second max
count = 0
value_list=[0]*100
for key,value in candidates.items():
    print(value)
    print(count)
    value_list[count] = value
    count+=1
first = max(value_list)
indx_max = value_list.index(max(value_list))

value_list.pop(indx_max)
second = max(value_list)

#print the final results
for key,value in candidates.items():
     
    print("{}: {:.2f}% ({})".format(key,100*value/voterNum,value))
    print("{}: {:.2f}% ({})".format(key,100*value/voterNum,value),file=elec_result)
    if(value==first):
        first_candi = key
    elif(value == second):
        second_candi = key

print("---------------------------------------")
print("1st Advancing Candidate: {}".format(first_candi))
print("2st Advancing Candidate: {}".format(second_candi))
print("---------------------------------------")

print("---------------------------------------",file=elec_result)
print("1st Advancing Candidate: {}".format(first_candi),file=elec_result)
print("2st Advancing Candidate: {}".format(second_candi),file=elec_result)
print("---------------------------------------",file=elec_result)

#close the output file
elec_result.close()