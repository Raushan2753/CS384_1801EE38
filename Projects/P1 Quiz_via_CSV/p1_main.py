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

# now defining function which will print all the 7 data which will be shown throughout the quiz
def print_user_data(data, skipped):
    os.system('cls')
    print(f"Roll: {data[1]}\nName: {data[0]}")
    print(f"Unattempted Questions: ", skipped_questions)
    print("Goto Question: Press Ctrl+Alt+G")
    print("Final Submit: Press Ctrl+Alt+F")
    print("Export Database into CSV: Press Ctrl+Alt+E")
    print()

# Now defining function which will print the marks from the database
def print_marks_from_database(roll_no):
    os.chdir(path)
    con = sqlite3.connect('project1 quiz cs384.db')
    cursor_ = con.cursor()

    users_data = []
    for row in cursor_.execute("SELECT * FROM project1_marks WHERE quiz_no=?", (roll_no,)):
        users_data.append(row)

    print(users_data)

def save_marks_in_database(roll_no, quiz_no, marks):
    os.chdir(path)
    con = sqlite3.connect('project1 quiz cs384.db')
    cursor_ = con.cursor()
    data = (roll_no, quiz_no)
    try:
        cursor_.execute(
            """CREATE TABLE project1_marks
	    	         (roll text, quiz_no integer(2), marks integer(3))"""
        )
    except:
        pass
    typeof = type(marks)
    if not typeof == int:
    	mark = marks.item()
    else:
    	mark = marks
    cursor_.execute("DELETE FROM project1_marks WHERE roll=? AND quiz_no=?", data)
    cursor_.execute("INSERT INTO project1_marks VALUES (?,?,?)",
              (roll_no, quiz_no, mark))
    con.commit()
    con.close()

def export_to_csv():
	for i in range(1,4):
		fileName = f"quiz{i}.csv"
		con = sqlite3.connect('project1 quiz cs384.db')
		cursor_ = con.cursor()
		data = []
		for row in cursor_.execute("SELECT * FROM project1_marks WHERE quiz_no=?", (i,)):
			data.append(row)
		if not data == []:
			with open(os.path.join(path, "quiz_wise_responses", fileName), "w") as file:
				writer = csv.writer(file)
				writer.writerow(["Roll No.", "Quiz No.", "Marks"])
				writer.writerows(data)

def start_quiz(quiz, user):
    roll_no = user[1]
    quiz_no = quiz
    questions_folder = os.path.join(path, "quiz_wise_questions")
    responses_folder = os.path.join(path, "quiz_wise_responses")
    individual_folder = os.path.join(path, "individual_responses")

    csv_file = "q"+str(quiz_no)+".csv"
    os.chdir(questions_folder)
    quiz_file = pd.read_csv(csv_file)
    count=0
    tmp = ''
    #defining a list which will store the skipped questions
    global skipped_questions
    marks_quiz, skipped_questions, responses_for_csv = [], [], []
    no_of_skipped_questions, correct, wrong, total_marks = 0, 0, 0, 0
    show_skipped = False

    while count < quiz_file.shape[0]:
        count += 1
        marks_gained = 0
        print_user_data(user, show_skipped)
        # print()
        print(f"    Question {count}) {quiz_file.question[count-1]}")
        print(f"Option 1) {quiz_file.option1[count-1]}")
        print(f"Option 2) {quiz_file.option2[count-1]}")
        print(f"Option 3) {quiz_file.option3[count-1]}")
        print(f"Option 4) {quiz_file.option4[count-1]}")
        print()
        print(
            f"    Credits if Correct Option: {quiz_file.marks_correct_ans[count-1]}")
        print(f"Negative Marking: {quiz_file.marks_wrong_ans[count-1]}")
        compulsion_map = {'n': "No", 'y': "Yes"}
        print(
            f"Is compulsory: {compulsion_map[quiz_file.compulsory[count-1]]}")
        print()

        if compulsion_map[quiz_file.compulsory[count-1]] == "Yes":
            print("   Enter Choice (1, 2, 3, 4):  ")
            tmp = hotkeys()
        else:
            print("   Enter Choice (1, 2, 3, 4, S):  ")
            tmp = hotkeys()
        time.sleep(0.5)

        if tmp == str(quiz_file.correct_option[count-1]):
            marks_gained = quiz_file.marks_correct_ans[count-1]
            correct += 1
        elif tmp == 's':
            skipped_questions.append(count)
            no_of_skipped_questions += 1
            marks_gained = 0
        elif tmp == 'export_to_csv':
        	count -= 1
        	export_to_csv()
        	marks_gained = 0
        elif tmp == 'skip_question':
        	count -= 1
        	show_skipped = True
        elif tmp == 'goto_question':
            count = int(input("Goto the question no. :"))
            count -= 1
            continue
        elif tmp == 'final_submit':
        	count -= 1
        	break
        else:
            marks_gained = quiz_file.marks_wrong_ans[count-1]
            wrong += 1
        marks_quiz.append(marks_gained)
        
        if (not count<1) and tmp in ['1','2','3','4','s']:
	        total_marks += quiz_file.marks_correct_ans[count-1]
	        extra = [tmp]
	        responses_for_csv.append(list(quiz_file.loc[count-1][0:-1]))
	        responses_for_csv[count-1] += extra
    header_responses = quiz_file.columns.values
    header_responses = list(header_responses)[:-1]

    additional_header = ['marked choice']
    header_responses = header_responses + additional_header
    os.chdir(path)
    os.chdir(os.path.join(path, "individual_responses"))
    total_marks_obtained = sum(marks_quiz)
    additional_col = {
        "Total": [correct, wrong, no_of_skipped_questions, total_marks_obtained, total_marks],
        "Legend": ["Correct Choices", "Wrong Choices", "Unattempted", "Marks Obtained", "Total Quiz Marks"]
    }
    new_df = pd.DataFrame(additional_col)
    responses_df = pd.DataFrame(responses_for_csv, columns=header_responses)
    header_responses += ["Total", "Legend"]
    responses_df = pd.concat([responses_df, new_df], axis=1)

    responses_csv_name = "q" + str(quiz_no) + "_" + roll_no + ".csv"
    responses_df.to_csv(responses_csv_name, index=False)

    save_marks_in_database(roll_no, quiz_no, total_marks_obtained)

    print_user_data(user, show_skipped)
    print(f"Total Quiz Questions: {count}")
    print(f"Total Quiz Questions Attempted: {count - no_of_skipped_questions}")
    print(f"Total Correct Questions: {correct}")
    print(f"Total Wrong Questions: {wrong}")
    print(f"Total Marks Questions: {total_marks_obtained}/{total_marks}\n")