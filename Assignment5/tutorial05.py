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


def rename_Game_of_Thrones(paddingseason, paddingepisode):
    # rename Logic
    series_path = r'./Subtitles/Game of Thrones'
    file_compile = os.listdir(series_path)
    for series in file_compile:
        split_series = series.split(' - ')
        season_no = split_series[1][0:split_series[1].index('x')]
        episode_no = split_series[1][split_series[1].index('x')+1:]
        episode_name = split_series[2][0:split_series[2].index('.')]
        extension = (re.split(r'\.',split_series[2])[-1]).strip()
        while(len(season_no) < paddingseason):
            season_no = '0'+season_no
        if(len(season_no) > paddingseason):
            season_no = season_no[-1*paddingseason:]
        while(len(episode_no) < paddingepisode):
            episode_no = '0'+episode_no
        if(len(episode_no) > paddingepisode):
            episode_no = episode_no[-1*paddingepisode:]
        try:
            os.rename(series_path+'/'+series, series_path+'/' +split_series[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.'+extension)
        except:
            os.remove(series_path+'/'+series)
    pass

def rename_Sherlock(paddingseason, paddingepisode):
    # rename Logic
    series_path = r'./Subtitles/Sherlock'
    file_compile = os.listdir(series_path)
    for series in file_compile:
        temp = series[series.index('.')+1:]
        season_no = temp[1]+temp[2]
        temp2 = temp[temp.index('E')+1:]
        episode_no = temp2[0]+temp2[1]
        extension = (re.split(r'\.',series)[-1]).strip()
        while(len(season_no) < paddingseason):
            season_no = '0'+season_no
        if(len(season_no) > paddingseason):
            season_no = season_no[-1*paddingseason:]
        while(len(episode_no) < paddingepisode):
            episode_no = '0'+episode_no
        if(len(episode_no) > paddingepisode):
            episode_no = episode_no[-1*paddingepisode:]
        try:
            os.rename(series_path+'/'+series, series_path+'/' +'Sherlock - Season '+season_no+' Episode '+episode_no+'.'+extension)
        except:
            os.remove(series_path+'/'+series)
    pass

def rename_Suits(paddingseason, paddingepisode):
    # rename Logic
    series_path = r'./Subtitles/Suits'
    file_compile = os.listdir(series_path)
    for series in file_compile:
        split_series = series.split(' - ')
        season_no = split_series[1][0:split_series[1].index('x')]
        episode_no = split_series[1][split_series[1].index('x')+1:]
        temp1 = split_series[2].split('.480')
        temp2 = temp1[0].split('.720')
        temp3 = temp2[0].split('.1080')
        temp4 = temp3[0].split('.HDTV')
        episode_name = temp4[0].split('.en')[0]
        extension = (re.split(r'\.',series)[-1]).strip()
        while(len(season_no) < paddingseason):
            season_no = '0'+season_no
        if(len(season_no) > paddingseason):
            season_no = season_no[-1*paddingseason:]
        while(len(episode_no) < paddingepisode):
            episode_no = '0'+episode_no
        if(len(episode_no) > paddingepisode):
            episode_no = episode_no[-1*paddingepisode:]
        try:
            os.rename(series_path+'/'+series, series_path+'/' +
                          split_series[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.'+extension)
        except:
            os.remove(series_path+'/'+series)
    pass
    
def rename_How_I_Met_Your_Mother(paddingseason, paddingepisode):
    # rename Logic
    series_path = r'./Subtitles/How I Met Your Mother'
    file_compile = os.listdir(series_path)
    for series in file_compile:
        split_series = series.split(' - ')
        season_no = split_series[1][0:split_series[1].index('x')]
        episode_no = split_series[1][split_series[1].index('x')+1:]
        temp1 = split_series[2].split('.480')
        temp2 = temp1[0].split('.720')
        temp3 = temp2[0].split('.1080')
        temp4 = temp3[0].split('.HDTV')
        episode_name = temp4[0].split('.en')[0]
        extension = (re.split(r'\.',series)[-1]).strip()
        while(len(season_no) < paddingseason):
            season_no = '0'+season_no
        if(len(season_no) > paddingseason):
            season_no = season_no[-1*paddingseason:]
        while(len(episode_no) < paddingepisode):
            episode_no = '0'+episode_no
        if(len(episode_no) > paddingepisode):
            episode_no = episode_no[-1*paddingepisode:]
        try:
            os.rename(series_path+'/'+series, series_path+'/' +
                          split_series[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.'+extension)
        except:
            os.remove(series_path+'/'+series)
    pass

    