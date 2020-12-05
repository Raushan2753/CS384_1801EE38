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

def register_login():

    reg_users = database_data()
    reg_roll_no = []
    for r in reg_users:
        reg_roll_no.append(r[1])

    name = ""
    roll_no = ""
    password = ""
    contact_no = 0

    username = input("Username: ")
    if username in reg_roll_no:
        password = gp.getpass("Password:")

        if bcrypt.checkpw(password.encode('utf-8'), reg_users[reg_roll_no.index(username)][2]):
            print("Succesfully logged in!")
            return reg_users[reg_roll_no.index(username)]
        else:
            print("Wrong Password")
            register_login()
    else:
        print("User is not registered. Kindly register.")
        name = input("Name: ")
        roll_no = input("Roll No.: ")
        contact_no = int(input("Contact No.: "))
        password = gp.getpass("Password:")
        hashable_pw = bytes(password, encoding="utf-8")
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        con = sqlite3.connect("project1 quiz cs384.db")
        cursor_ = con.cursor()
        cursor_.execute(
            "INSERT INTO project1_registration VALUES (?,?,?,?)",
            (name, roll_no, hashed_pw, contact_no),
        )
        con.commit()
        con.close()
        print("Successfully registered!")
        return (name, roll_no, hashed_pw, contact_no)

def hotkeys():
    tmp = ''
    while detect_keypress:
        try:
            if keyboard.is_pressed('ctrl+alt+u') or keyboard.is_pressed('ctrl+alt+U'):
                tmp = 'skip_question'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+g') or keyboard.is_pressed('ctrl+alt+G'):
                tmp = 'goto_question'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+f') or keyboard.is_pressed('ctrl+alt+F'):
                end_quiz = True
                end_timer = True
                tmp = 'final_submit'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+e') or keyboard.is_pressed('ctrl+alt+E'):
                tmp = 'export_to_csv'
                return tmp
            elif keyboard.is_pressed('1'):
            	tmp = '1'
            	print("1")
            	return tmp
            elif keyboard.is_pressed('2'):
            	tmp = '2'
            	print("2")
            	return tmp
            elif keyboard.is_pressed('3'):
            	tmp = '3'
            	print("3")
            	return tmp
            elif keyboard.is_pressed('4'):
            	tmp = '4'
            	print("4")
            	return tmp
            elif keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            	tmp = 's'
            	print("s")
            	return tmp
            elif keyboard.is_pressed('ctrl+q') or keyboard.is_pressed('ctrl+Q'):
            	tmp = 'q'
            	return tmp
        except:
            print("an error occured")
            break

