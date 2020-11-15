import csv
import os
import shutil
import re

def rename_FIR(paddingepisode, paddingseason=0):
    # rename Logic
    series_path = r'./Subtitles/FIR'
    file_compile = os.listdir(series_path)
    for series in file_compile:       
        # Now finding all integer in series name
        int_in_series = re.compile(r'\d+')
        list_of_int = re.findall(int_in_series,series)
        # now list_of_int[0] will be the episode number
        episode_number = list_of_int[0]
        extension = (re.split(r'\.',series)[-1]).strip()
        while(len(episode_number) < paddingepisode):
            episode_number = '0'+episode_number
        if(len(episode_number) > paddingepisode):
            episode_number = episode_number[-1*paddingepisode:]
        try:
            os.rename(series_path+'/'+series,series_path+'/'+'FIR'+' - Episode '+episode_number+'.'+extension)
        except:
            os.remove(series_path+'/'+series)
    pass


def rename_Game_of_Thrones(folder_name):
    # rename Logic 
    

def rename_Sherlock(folder_name):
    # rename Logic 
    

def rename_Suits(folder_name):
    # rename Logic 
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    