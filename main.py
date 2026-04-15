from extractFeatures import extractfeatures
from fileLoader import load_audio_files
from storage_handler import write_csv, read_csv
from pitchAnalysis import meanMedian
from Plotting import plotmeans 
from checklength import checklength 
import os.path


def csv_handler( fname, filenames):

    if os.path.exists(fname): #Checks if the csv already exists 
        dict= read_csv(fname) #if it exists it gets writen to a dictionary 
    else: 
        Mean, Median, features= extractfeatures(filenames, names) #extracts average, min and max pitch and saves to dic
        write_csv (features, fname) #writes above dict to a csv 
        dict= read_csv(fname) #reads in the csv as a dict
    return (dict)

if __name__ == "__main__":

    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 
    #define the folder that the stimuli are stored in 
    foldername= 'FixLengthShift'
    #define the name of the csv that will be generated 
    fname = (r".\PitchAnalysis.csv")

    audio_files, GibFiles, IEEEFiles = load_audio_files(foldername, names) # function creats a list of mp3s in the folder 

    checklength (GibFiles, IEEEFiles)



    dict= csv_handler(fname, audio_files) #read in csv that has mean and median data 
    print(dict)
    outliers=meanMedian(dict) #calculate outliers
    fig = plotmeans(dict) #lots mean and median for each group 




    



    #getpitchinfo(GibFiles, names, 'GibMean.csv', 'GibMedians.csv','Gibdict.csv' )
   # GibMeans, GibMedians, Gibdict= extractfeatures(GibFiles, names)




















    
