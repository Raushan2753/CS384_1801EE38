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



