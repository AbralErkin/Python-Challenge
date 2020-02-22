#import the libraries
import os
import csv
from statistics import mean

#extract the file path
file_path = os.path.join('.','budget_data.csv')
#open file to output the results
finance_result = open("Budget_Data_Results.txt","w")

#initialize the list 
budget_date=[]
prof_list = []

#initialize the total number of voters
totalNum = 0
totalProf = 0


#open the csv file
with open(file_path,'r') as csv_file:

    #read the csv file and assign the content to the variable
    csv_reader = csv.reader(csv_file,delimiter=',')

    #remove the headers
    next(csv_reader)

    #count the number of voters for each candidate and save it to the dictionary
    for row in csv_reader:
        budget_date.append(row[1])
        totalProf += int(row[0])
        prof_list.append(int(row[0]))
        totalNum +=1
#calculate average change
change_list = [x-prof_list[i-1] for i,x in enumerate(prof_list) if i >0]
change_aver = mean(change_list)

#find the maximum increase and maximum decrease values
inc_mx = max(change_list)
dec_mx = min(change_list)

#find the maximum increase and maximum decrease months
inc_date = budget_date[change_list.index(inc_mx)+1]
dec_date = budget_date[change_list.index(dec_mx)+1]

#print the results to the screen
print("Financial Analysis\n")
print("---------------------------\n")
print("Total Months: {}".format(totalNum))
print("Total: ${}".format(totalProf))
print("Average Change: ${:.2f}".format(change_aver))
print("Greatest Increase in Profits: {} (${})".format(inc_date,inc_mx))
print("Greatest Decrease in Profits: {} (${})".format(dec_date,dec_mx))

#print the results to the file
print("Financial Analysis\n",file=finance_result)
print("---------------------------\n",file=finance_result)
print("Total Months: {}".format(totalNum),file=finance_result)
print("Total: ${}".format(totalProf),file=finance_result)
print("Average Change: ${:.2f}".format(change_aver),file=finance_result)
print("Greatest Increase in Profits: {} (${})".format(inc_date,inc_mx),file=finance_result)
print("Greatest Decrease in Profits: {} (${})".format(dec_date,dec_mx),file=finance_result)
#close the output file
finance_result.close()
