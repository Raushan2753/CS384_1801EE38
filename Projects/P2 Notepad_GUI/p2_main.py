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

#FILE MENU functions!
def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)
    on_content_changed()

def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML", "*.html"),("CSS", "*.css"),("JavaScript", "*.js"),("Python", "*.py")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())
    
    on_content_changed()
     
def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass  

def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(initialfile ='untitle.txt',defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML", "*.html"),("CSS", "*.css"),("JavaScript", "*.js"),("Python", "*.py")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"
    
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Exit", "Are you sure you want to Quit?"):
        root.destroy()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
# EDIT MENU functions!

def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"
def copy():
    content_text.event_generate("<<Copy>>")
    on_content_changed()
    return "break"
def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"

def selectall(event=None):
    content_text.tag_add('sel','1.0','end')
    return "break"
   
# find & replace functionality 

def find_func(event=None):
##using tag inbuilt function
    def find():
        word = find_input.get()
        content_text.tag_remove('match','1.0',END)
        matches = 0
        if word :
            start_pos = '1.0'
            while True :
                start_pos = content_text.search(word,start_pos,stopindex=END)
                if(not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                content_text.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                content_text.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = content_text.get(1.0,END)
        new_content = content.replace(word,replace_text)
        content_text.delete(1.0,END)
        content_text.insert(1.0,new_content)


    find_dialogue = Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0,0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text ='Find/Replace')
    find_frame.pack(pady=20)

    ## labels 
    text_find_label = ttk.Label(find_frame,text ='Find :')
    text_replace_label = ttk.Label(find_frame,text ='Replace')

    ##entry boxes 
    find_input = ttk.Entry(find_frame,width=30)
    replace_input = ttk.Entry(find_frame,width=30)


    ## Button
    find_button = ttk.Button(find_frame,text ='Find',command=find)
    replace_button = ttk.Button(find_frame,text ='Replace',command=replace)

    ##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    ##entry grid
    find_input.grid(row=0, column=1,padx=4,pady=4)
    replace_input.grid(row=1, column=1,padx=4,pady=4)

    ##button grid
    find_button.grid(row=2 ,column=0 ,padx=8,pady=4)
    replace_button.grid(row=2 ,column=1 ,padx=8,pady=4)

    find_dialogue.mainloop()    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#ABOUT MENU funtions!

def display_about(event=None):
    tkinter.messagebox.showinfo(
        "About", PROGRAM_NAME + "\nA simple Notepad made in Python with Tkinter\n In which you can change theme,color,font,size,etc\n and can find or replace a specific line/word!!!\n Credits:~Raushan/Rishabh")
def display_help(event=None):
    tkinter.messagebox.showinfo(
        "Help", "This Text Editor works similar to any other editors.",
        icon='question')
def rate():
    value=tkinter.messagebox.askquestion(" was your experience good ?","Do you like our noob 'Notepad' ?")
    if(value=="yes"):
        msg="Thank You :)"
    else :
        msg="Sorry :( ,please let us know,How we can improve"
    tkinter.messagebox.showinfo("Experience",msg)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#_some extra features!

#_adding Line Numbers Functionality!
def get_line_numbers():
    output = ''
    if show_cursor_info.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output
def on_content_changed(event=None):
    update_cursor()

# Adding Cursor Functionality!
def show_cursor():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='yes', fill=X, side=BOTTOM, anchor='se')
    else:
        cursor_info_bar.pack_forget()
def update_cursor(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)                
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)

#font family

def change_font(root):
    global font_now
    font_now=font_family.get()
    content_text.configure(font= (font_now,font_size_now))

def change_size(root):
    global font_size_now
    font_size_now =size_variable.get()
    content_text.configure(font= (font_now,font_size_now)) 
   

#_Adding Text Highlight Functionality!
def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add(
        "active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)
def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")
def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()

#_Adding Change Theme Functionality!
def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(
        background=background_color, fg=foreground_color)
#pop-up menu
def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)

# status bar
status_bar = ttk.Label(root, text ='Status Bar')
status_bar.pack(side=BOTTOM)

text_changed = False

def changed(event=None):
    global text_changed
    if content_text.edit_modified():###checks if any character is added or not
        text_changed= True
        words = len(content_text.get(1.0, 'end-1c').split()) ##it even counts new line character so end-1c subtracts one char
        characters = len(content_text.get(1.0,'end-1c'))
        status_bar.config(text=f' Words: {words} Characters : {characters}')
    content_text.edit_modified(False)
content_text.bind('<<Modified>>',changed)

url = ''
def modification_time():
    global url
    url = os.getcwd()
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(url)))
    tkinter.messagebox.showinfo('Modified time','Last Modified at: ' + str(modificationTime))

def creation_time():
    global url
    url = os.getcwd()
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(url)))
    tkinter.messagebox.showinfo('creation time: ', 'Created at: ' + str(modificationTime))  
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#                                              
                                                    ###!MENU CODES GOES HERE!###

#File menue begins!
menu_bar = Menu(root) 
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', underline=0, command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', underline=0, command=open_file)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', underline=0, command=save)
file_menu.add_command(label="Save As", accelerator='Ctrl+Shift+S', compound='left', underline=0, command = save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)
# end of File Menu!
#Edit menue begins!
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left',  underline=0, command=cut) 
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', underline=0, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left',  underline=0, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find \& Replace', accelerator='Ctrl+F', compound='left', underline=0, command=find_func) 
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0, command=selectall) 
menu_bar.add_cascade(label='Edit', menu=edit_menu)
#end of Edit Menu!

#view menue 
view_menu = Menu(menu_bar, tearoff=0)
show_cursor_info=IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor)
to_highlight_line=IntVar()
view_menu.add_checkbutton(label='Highlight Current Line', variable=to_highlight_line, onvalue=1, offvalue=0,command=toggle_highlight)
themes_menu=Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu, command=change_theme)
''' THEMES OPTIONS'''
color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}
theme_choice=StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k, variable=theme_choice, command=change_theme)
menu_bar.add_cascade(label='View', menu=view_menu)


#start of About Menu!
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About', underline=0, command=display_about)
about_menu.add_command(label ='Rate us',underline =0,command =rate)
about_menu.add_command(label='Help', underline=0, command=display_help)
root.config(menu=menu_bar)
#end of About Menu!
#Stats menue begins!
stats_menu = Menu(menu_bar, tearoff=0)
stats_menu.add_command(label="Modified Time", compound=LEFT,command= modification_time)
stats_menu.add_command(label="Creation Time", compound=LEFT,command=creation_time)
menu_bar.add_cascade(label='Stats', menu=stats_menu)
# end of stats menu
#adding top shortcut bar 
shortcut_bar=Frame(root, height=25)
shortcut_bar.pack(expand='no', fill='x')

#adding Scrollbar Widget!

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='both')
# adding cursor info label!
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1',background='green')
cursor_info_bar.pack(expand='yes', fill=X, side=BOTTOM,anchor='se')

# setting up the pop-up menu!
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=selectall)
content_text.bind('<Button-3>', show_popup_menu)

#setting up font and size!
font_tuple=tkinter.font.families()
font_family=tkinter.StringVar()
font_box=ttk.Combobox(tool_bar_label,width=30,textvariable = font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=2,pady=3)

size_variable=tkinter.IntVar()
font_size=ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state="readonly")
font_size["values"]=tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=3)

font_now="Arial"
font_size_now=12

#binding combobox with function of font & size!
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)


#handling binding!
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-A>',selectall)
content_text.bind('<Control-a>',selectall)
content_text.bind('<KeyPress-F1>', display_help)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory2')
content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()

                                                         ###END OF MENU##
#########################################################################################################################################################################
root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()