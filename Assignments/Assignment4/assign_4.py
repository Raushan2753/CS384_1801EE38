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
