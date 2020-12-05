from tkinter import*
import os
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk,font
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import time
root = Tk()
file = Menu(root) 
#root.iconbitmap('icon.ico')
PROGRAM_NAME = "Noob Notepad"
root.title(PROGRAM_NAME)
file_name = None
root.geometry('800x400')
tool_bar_label=ttk.Label(root,background="red")
tool_bar_label.pack(side=TOP,fill='x')
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both') 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                        #__All codes goes Here__#
