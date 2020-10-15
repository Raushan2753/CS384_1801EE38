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

def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
