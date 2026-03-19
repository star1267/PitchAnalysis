import os 
import pathlib
def load_audio_files(foldername):
    """ This function creates a list of all the Mp3s in a folder"""
    audio_files = [] #empty list
    print (audio_files)
    os.chdir(foldername)
    for filename in os.listdir(path = '.'): #loops through each file
        if filename.endswith(".wav"): #checks if it ends with mp3
            audio_files.append(os.path.join(filename)) #if it is an mp3 it adds it to the list 
    return audio_files #returns the list

    ...