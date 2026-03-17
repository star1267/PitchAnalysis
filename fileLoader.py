import os 

def load_audio_files(directory):
    """ This function creates a list of all the Mp3s in a folder"""
    audio_files = [] #empty list
    for filename in os.listdir(directory): #loops through each file
        if filename.endswith(".mp3"): #checks if it ends with mp3
            audio_files.append(os.path.join(filename)) #if it is an mp3 it adds it to the list 
    return audio_files #returns the list

    ...