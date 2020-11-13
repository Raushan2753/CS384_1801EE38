import csv
import os
import shutil
import re

#defining sort function which will take list as an argument and sort the list according to semester number
def sort_acc_to_sem(lis):
    return lis[4]

# If Grade directory was already there then I am deleting that directory using shutill.rmtree
if(os.path.isdir(r'./grades')):
    shutil.rmtree('./grades')

roll_no=re.compile(r'^[0-9]{4}[A-Za-z]{2}[0-9]{2}$')
sem_credit=re.compile(r'^[0-9]+$')
sub_code = re.compile(r'^[A-Z]{2}[0-9]{3}$',re.IGNORECASE)
credit_obtained=re.compile(r'AA|AB|BC|BB|CC|CD|DD|I|F',re.IGNORECASE)
grades = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}
header=['sl','roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']
# Now create grade directory
cd = os.getcwd()
path_grades = os.path.join(cd,'grades')
if(os.path.exists(path_grades)==False):
    os.mkdir(path_grades)
file=open('./grades/misc.csv','a',newline='')
with file:
    writer=csv.writer(file)
    writer.writerow(header)
#creating an empty list to store the details of performance
roll_no_list = []
# Now open the acad_res_stud_grades.csv file in read mode
file = open('./acad_res_stud_grades.csv', 'r')
with file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(not row[0]=='sl'):
            if(not (re.fullmatch(roll_no,row[1]) and re.fullmatch(sem_credit,row[2]) and re.fullmatch(sub_code,row[4]) and re.fullmatch(sem_credit,row[5]) and re.fullmatch(credit_obtained,row[6]))):
                file=open('./grades/misc.csv','a',newline='')
                with file:
                    writer=csv.writer(file)
                    writer.writerow(row)
                continue
            # Naming the csv file with name as roll_no+individual.csv
            roll_no_csv_file = row[1] + '_individual.csv'
            # if csv file with the given roll no do not exist then store the details in list then
            # create the csv file then write Roll no and header into it then write the details of that rooll no
            if(not os.path.isfile('./grades/'+roll_no_csv_file)):
                roll_no_list.append(row[1])
                file1 = open('./grades/'+roll_no_csv_file, 'a',newline='')
                with file1:
                    writer=csv.writer(file1)
                    writer.writerow(['Roll: '+row[1]])
                    writer.writerow(['Semester Wise Details'])
                    writer.writerow(['Subject','Credits','Type','Grade','Sem'])
            # Now creating another list which store the performace details
            perf_detail_list = [row[4],row[5],row[8],row[6],row[2]]
            file2 = open('./grades/'+roll_no_csv_file, 'a',newline='')
            with file2:
                writer=csv.writer(file2)
                writer.writerow(perf_detail_list)
