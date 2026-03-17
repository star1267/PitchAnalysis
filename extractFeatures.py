import os 
import parselmouth

def extractfeatures(audio_file, directory):
    os.chdir(directory)   #navigates to the folder where the files are
    length = len(audio_file) #counts number of files
    dict = {} #creates empty dict
    for f in range(length): #loops through each mp3
    
        audio = audio_file[f] #selects audio
        sound = parselmouth.Sound(audio) #converts it to a sound
        pitch = sound.to_pitch() #gets the pitch information
        pitch_mean = parselmouth.praat.call(pitch, "Get mean", 0, 0, "Hertz") #calculate mean
        pitch_min = parselmouth.praat.call(pitch, "Get minimum", 0, 0, "Hertz", "Parabolic") #min
        pitch_max = parselmouth.praat.call(pitch, "Get maximum", 0, 0, "Hertz", "Parabolic") #max

        #write a dictionary 
        dict[f] = {
            "filename": audio,
            "meanPitch": pitch_mean,
            "MinPitch": pitch_min,
            "MaxPitch": pitch_max,
        }
        ...
    return dict