
from extractFeatures import extractfeatures
from fileLoader import load_audio_files
from storage_handler import write_csv

def main( ):
    directory = r'C:\Users\testarr\Documents\pythoncode\pitch-change\StimuliSamples' #set directory 
    audio_file= load_audio_files(directory) # function creats a list of mp3s in the folder 
    dict= extractfeatures(audio_file, directory) #extracts average, min and max pitch and saves to dic
    write_csv (dict) #writes above dict to a csv 
    
if __name__ == "__main__":
    main()
