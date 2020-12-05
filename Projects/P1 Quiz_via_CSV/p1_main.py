import os
import time
import sqlite3
import keyboard
import threading
import csv
import bcrypt
import re
import getpass as gp
import pandas as pd
from tkinter import *

def database_data():
    data = []
    db_file = sqlite3.connect("project1 quiz cs384.db")
    cursor_ = db_file.cursor()

    try:
        cursor_.execute(
            """CREATE DATABASE of project1_registration
	    	         (name text, roll text, password text, contact integer(10))"""
        )
    except:
        pass

    for r in cursor_.execute("SELECT * FROM project1_registration"):
        data.append(r)
    db_file.close()

    return data


global path
path = os.getcwd()

global end_timer, detect_keypress
end_timer, detect_keypress = False, True

global unattempted_ques
unattempted_ques = []

def timer(quiz):

    time_detail = 0
    root = Tk()
    root.geometry("300x90")
    root.title("Time Remaining")
    with open(os.path.join(path, "quiz_wise_questions", f"q{quiz}.csv"), "r") as file:
    	reader = csv.reader(file)
    	for r in reader:
    		time_detail = r[10]
    		file.close()
    		break
    tt = re.findall('\d+', time_detail)

    minute = StringVar()
    second = StringVar()
    # set initial time
    minute.set("00")
    second.set("00")

    minuteEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=100, y=20)

    secondEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=second)
    secondEntry.place(x=150, y=20)
    
    t = (int(tt[0]))*60
    
    while t > -1:
        mins, secs = divmod(t, 60)
        if end_timer:
        	root.destroy()
        	break
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        t -= 1