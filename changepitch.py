from fileLoader import load_audio_files
from pitchHandler import pitchshift


def manipulatevoices(Files, newfolder): 
    pitchshift(Files['Bella'], 0.8, newfolder, storagefolder)  
    pitchshift(Files['River'], 1.2, newfolder, storagefolder)  
    pitchshift(Files['Clancy'], 1.09, newfolder, storagefolder)  
    pitchshift(Files['Matt'], 0.9, newfolder, storagefolder)  



if __name__ == "__changepitch__":
    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 


    #define the folder that the stimuli that has the stim you want to change 
    storagefolder= 'FinalWav'

    audio_files, GibFiles, IEEEFiles = load_audio_files(storagefolder, names) # function creats a list of wav files in the folder 

    newfolder = "ShiftedSecond"
    manipulatevoices(IEEEFiles, newfolder)
    manipulatevoices(GibFiles, newfolder)
    print ("Files made")


    