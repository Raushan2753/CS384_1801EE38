import csv
import os
import re
import shutil
import datetime

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if(os.path.isdir(r'./analytics')):
        shutil.rmtree('./analytics')
    os.makedirs('./analytics')
    pass


def degree_name(str):
    if (str == '01'):
        return 'btech'
    elif (str == '11'):
        return 'mtech'
    elif (str == '12'):
        return 'msc'
    elif (str == '21'):
        return 'phd'

def course():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        course_path = os.path.join(path_analytics,'course')
        if(os.path.exists(course_path)==False):
            os.mkdir(course_path)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        roll_no_match = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')
        for row in stud_file:
            roll_no = row['id']
            if(len(row['id']) == 8 and re.match(roll_no_match,row['id'])):
                dept = row['id'][4:6]
                dept = dept.lower()
                dept_path = os.path.join(course_path,dept)
                if(os.path.exists(dept_path) == False):
                    os.mkdir(dept_path)

                if(row['id'][2:4] in ['01','11','12','21']): # Checking the degree (btech/mtech/mse/phd)
                    degree_code = str(roll_no[2:4])
                    degree = degree_name(degree_code)
                    degree_path = os.path.join(dept_path,degree)
                    if(os.path.exists(degree_path) == False):
                        os.mkdir(degree_path)

                    
                    Enroll_year = str(roll_no[0:2])
                    file_name = Enroll_year + '_' + dept + '_' + degree + '.csv'
                    file_path = os.path.join(degree_path,file_name)

                    if (os.path.exists(file_path) == False):
                        with open(file_path,'a') as file1:
                            writer = csv.DictWriter(file1,fieldnames = header)
                            writer.writeheader()
                            writer.writerow(row)
                    else :
                        with open(file_path, 'a') as file2:
                            writer = csv.DictWriter(file2, fieldnames = header)
                            writer.writerow(row)


                else:
                    misc_path = os.path.join(course_path,'misc.csv')
                    if (os.path.exists(misc_path) == False) :
                        with open(misc_path,'a') as file1 :
                            writer = csv.DictWriter(file1, fieldnames = header)
                            writer.writeheader()
                            writer.writerow(row)
                    else :
                        with open(misc_path, 'a') as file2 :
                            writer = csv.DictWriter(file2, fieldnames = header)
                            writer.writerow(row)


            else :
                misc_path = os.path.join(course_path,'misc.csv')
                if (os.path.exists(misc_path) == False) :
                    with open(misc_path,'a') as file1 :
                        writer = csv.DictWriter(file1, fieldnames = header)
                        writer.writeheader()
                        writer.writerow(row)
                else :
                    with open(misc_path, 'a') as file2 :
                        writer = csv.DictWriter(file2, fieldnames = header)
                        writer.writerow(row)
    pass




def country():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        country_path = os.path.join(path_analytics,'country')
        if(os.path.exists(country_path)==False):
            os.mkdir(country_path)
        for row in stud_file:
            country_name = row['country']
            country_name = country_name.lower()
            csv_country = country_name + '.csv'
            file_path = os.path.join(country_path,csv_country)
            if (os.path.exists(file_path) == False):
                with open(file_path,'a') as file1:
                    writer = csv.DictWriter(file1, fieldnames = header)
                    writer.writeheader()
                    writer.writerow(row)
            else :
                with open(file_path, 'a') as file2 :
                    writer = csv.DictWriter(file2, fieldnames = header)
                    writer.writerow(row)
    pass


def email_domain_extract():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        email_path = os.path.join(path_analytics,'email')
        if(os.path.exists(email_path)==False):
            os.mkdir(email_path)
        for row in stud_file:
            email_name = row['email']
            email_name = email_name.lower()
            left_part = email_name.find('@')
            right_part = email_name.find('.')
            domain = email_name[left_part+1:right_part]
            csv_domain = domain + '.csv'
            file_path = os.path.join(email_path,csv_domain)
            if (os.path.exists(file_path) == False):
                with open(file_path,'a') as file1:
                    writer = csv.DictWriter(file1, fieldnames = header)
                    writer.writeheader()
                    writer.writerow(row)
            else :
                with open(file_path, 'a') as file2 :
                    writer = csv.DictWriter(file2, fieldnames = header)
                    writer.writerow(row)
    pass



def gender():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        gender_path = os.path.join(path_analytics,'gender')
        if(os.path.exists(gender_path)==False):
            os.mkdir(gender_path)
        for row in stud_file:
            gender_name = row['gender']
            gender_name = gender_name.lower()
            csv_gender = gender_name + '.csv'
            file_path = os.path.join(gender_path,csv_gender)
            if (os.path.exists(file_path) == False):
                with open(file_path,'a') as file1:
                    writer = csv.DictWriter(file1, fieldnames = header)
                    writer.writeheader()
                    writer.writerow(row)
            else :
                with open(file_path, 'a') as file2 :
                    writer = csv.DictWriter(file2, fieldnames = header)
                    writer.writerow(row)

    pass



def dob():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        dob_path = os.path.join(path_analytics,'dob')
        if(os.path.exists(dob_path)==False):
            os.mkdir(dob_path)
        for row in stud_file:
            dob_name = row['dob']
            year_str = re.split('-',dob_name)[2]
            year = int(year_str)
            if (year>=1995 and year<=1999):
                csv_dob = 'bday_1995_1999' + '.csv'
            elif (year>=2000 and year<=2004):
                csv_dob = 'bday_2000_2004' + '.csv'
            elif (year>=2005 and year<=2009):
                csv_dob = 'bday_2005_2009' + '.csv'
            elif (year>=2010 and year<=2014):
                csv_dob = 'bday_2010_2014' + '.csv'
            elif (year>=2015 and year<=2020):
                csv_dob = 'bday_2015_2010' + '.csv'

            file_path = os.path.join(dob_path,csv_dob)
            if (os.path.exists(file_path) == False):
                with open(file_path,'a') as file1:
                    writer = csv.DictWriter(file1, fieldnames = header)
                    writer.writeheader()
                    writer.writerow(row)
            else :
                with open(file_path, 'a') as file2 :
                    writer = csv.DictWriter(file2, fieldnames = header)
                    writer.writerow(row)
    pass




def state():
    # Read csv and process
    file = open('studentinfo_cs384.csv', 'r')
    with file:
        stud_file = csv.DictReader(file,skipinitialspace = True)
        header = ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state']
        cd = os.getcwd()
        path_analytics = os.path.join(cd,'analytics')
        if(os.path.exists(path_analytics)==False):
            os.mkdir(path_analytics)
        state_path = os.path.join(path_analytics,'state')
        if(os.path.exists(state_path)==False):
            os.mkdir(state_path)
        for row in stud_file:
            state_name = row['state']
            state_name = state_name.lower()
            csv_state = state_name + '.csv'
            file_path = os.path.join(state_path,csv_state)
            if (os.path.exists(file_path) == False):
                with open(file_path,'a') as file1:
                    writer = csv.DictWriter(file1, fieldnames = header)
                    writer.writeheader()
                    writer.writerow(row)
            else :
                with open(file_path, 'a') as file2 :
                    writer = csv.DictWriter(file2, fieldnames = header)
                    writer.writerow(row)
    pass



def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
