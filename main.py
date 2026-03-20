from extractFeatures import extractfeatures
from fileLoader import load_audio_files
from storage_handler import write_csv, read_csv
from pitchAnalysis import meanMedian
import os.path

def csv_handler( fname):
    if os.path.exists(fname): 
        dict= read_csv(fname)
    else: 
        dict= extractfeatures(audio_file) #extracts average, min and max pitch and saves to dic
        write_csv (dict, fname) #writes above dict to a csv 
    return (dict)

if __name__ == "__main__":

    #define the folder that the stimuli are stored in 
    foldername= 'FinalWav'
    #define the name of the csv that will be generated 
    fname = (r".\FinalWav.csv")
    audio_file= load_audio_files(foldername) # function creats a list of mp3s in the folder 
    dict= csv_handler(fname)

    outliers=meanMedian(dict)






    
