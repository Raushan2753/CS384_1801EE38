import csv
import re
import shutil
import pandas as pd
import os
from math import floor

def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    stud_list = []
    # creating the empty map which store the branch and their student strengths
    branch_map = {}
    file = open(r'./'+filename, 'r')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if stud_list == []:
                stud_list = row
            else:
                # since 1st entry in each row is roll no so roll no will be row[0]
                roll_no = row[0]
                # roll no consists of the form 2000cs24 so roll_no[4:6] will represent the branch of the respective student
                branch_code = roll_no[4:6]
                branch_code = branch_code.upper()
                if branch_map.get(branch_code) == None:
                    # if the csv file is already there then remove the file
                    if os.path.isfile(r'./'+branch_code+'.csv'):
                        os.remove(r'./'+branch_code+'.csv')
                    file = open(r'./'+branch_code+'.csv', 'a+', newline="")
                    with file:
                        reader = csv.writer(file)
                        reader.writerow(stud_list)
                    branch_map[branch_code] = 1
                else:
                    branch_map[branch_code] +=1
                file = open(r'./'+branch_code+'.csv', 'a+', newline="")
                with file:
                    reader = csv.writer(file)
                    reader.writerow(row)
        batch_strengths = []
        for branch_code in branch_map.keys():
            batch_strengths.append([branch_code,branch_map[branch_code]])
        # now sorting the batch strengths according to their strengths
        batch_strengths = sorted(batch_strengths, key = lambda code: int(code[1]), reverse = True)
        file = open(r'.\branch_strength.csv', 'w', newline="")
        with file:
            reader = csv.writer(file)
            reader.writerow(["BRANCH_CODE", "STRENGTH"])
        for branch in batch_strengths:
            file = open(r'.\branch_strength.csv', 'a+', newline="")
            with file:
                reader = csv.writer(file)
                reader.writerow(branch)
    
    no_of_branch = len(batch_strengths)
    grouping = [[0 for i in range(no_of_branch+2)]
             for j in range(number_of_groups+1)]
    # now grouping will contain the group in column 1 and total in column 2
    grouping[0][0] = "group"
    grouping[0][1] = "total"
    for i in range(2, no_of_branch+2):
        grouping[0][i] = batch_strengths[i-2][0]
    
    no_of_group = len(str(number_of_groups))
    # Creating csv files of each group
    for i in range(1,number_of_groups+1):
        stud_no_group = no_of_group - len(str(i))
        grouping[i][0] = "Group_G"+'0'*stud_no_group+str(i)+".csv"
    each_group_no = []
    for i in range(len(batch_strengths)):
        for j in range(1, number_of_groups+1):
            grouping[j][i+2] = floor(batch_strengths[i][1]/number_of_groups)
        each_group_no.append(batch_strengths[i][1]-number_of_groups*(floor(batch_strengths[i][1]/number_of_groups)))
    # now distributing student in each group
    temp = 1
    for i in range(len(each_group_no)):
        while each_group_no[i] > 0:
            grouping[temp][i+2] += 1
            each_group_no[i] -= 1
            if temp == number_of_groups:
                temp = 1
            else:
                temp += 1
    for i in range(1, number_of_groups+1):
        for j in range(2, no_of_branch+2):
            grouping[i][1] += grouping[i][j]
    if os.path.isfile(r'./stats_grouping.csv'):
        os.remove(r'./stats_grouping.csv')
    file = open(r'./stats_grouping.csv', 'w', newline="")
    with file:
        reader = csv.writer(file)
        reader.writerows(grouping)
    for i in range(1, number_of_groups+1):
        file = open(r'./'+grouping[i][0], 'w', newline="")
        with file:
            reader = csv.writer(file)
            reader.writerow(["Roll", "Name", "Email"])
    for i in range(2, no_of_branch+2):
        group = pd.read_csv(r'./'+grouping[0][i]+'.csv')
        temp =0
        for j in range(1, number_of_groups+1):
            temp2 = group.iloc[temp:temp+grouping[j][i]]
            temp += grouping[j][i]
            file2 = temp2.values.tolist()
            file = open(r'./'+grouping[j][0], 'a+', newline="")
            with file:
                reader = csv.writer(file)
                reader.writerows(file2)


filename = "Btech_2020_master_data.csv"
number_of_groups = int(input("Enter No. of Groups : ", ))
group_allocation(filename, number_of_groups)