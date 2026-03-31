from extractFeatures import extractfeatures
from fileLoader import load_audio_files
from storage_handler import write_csv, read_csv
from pitchAnalysis import meanMedian
from Plotting import plotmeans 
from pitchHandler import pitchshift
import os.path

def csv_handler( fname, filenames):
    #// TODO rewrite dict in a way that makes more sense 
    if os.path.exists(fname): 
        dict= read_csv(fname)
    else: 
        dict= extractfeatures(filenames) #extracts average, min and max pitch and saves to dic
        write_csv (dict, fname) #writes above dict to a csv 
    return (dict)


def manipulatevoices(Files): 
    pitchshift(Files['Bella'], 0.9, "Shifted", foldername)  
    pitchshift(Files['River'], 1.1, "Shifted", foldername)  
    pitchshift(Files['Clancy'], 1.1, "Shifted", foldername)  
    pitchshift(Files['Matt'], 0.9, "Shifted", foldername)  


if __name__ == "__main__":

    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 
    #define the folder that the stimuli are stored in 
    foldername= 'Shifted'
    #define the name of the csv that will be generated 
    fname = (r".\Shifted.csv")
    audio_files, GibFiles, IEEEFiles = load_audio_files(foldername, names) # function creats a list of mp3s in the folder 
    dict= csv_handler(fname, audio_files) #read in csv that has mean and median data 
    outliers=meanMedian(dict) #calculate outliers
    fig = plotmeans(dict)



    #// TODO make a new script with the manipulation code 
    #manipulatevoices(IEEEFiles)
    #manipulatevoices(GibFiles)








    
