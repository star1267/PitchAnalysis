from extractFeatures import extractfeatures
from fileLoader import load_audio_files
from storage_handler import write_csv

def main( ):
    #define the folder that the stimuli are stored in 
    foldername= 'FinalWav'
    #define the name of the csv that will be generated 
    fname = (r".\FinalWav.csv")
    audio_file= load_audio_files(foldername) # function creats a list of mp3s in the folder 
    dict= extractfeatures(audio_file) #extracts average, min and max pitch and saves to dic
    write_csv (dict, fname) #writes above dict to a csv 
    
if __name__ == "__main__":
    main()
