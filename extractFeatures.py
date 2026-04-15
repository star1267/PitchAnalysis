
import parselmouth #package to extract pitch information
import numpy as np #package to get median

def extractfeatures(audio_file, names):
    length = len(audio_file) #counts number of files
    dict = {} #creates empty dict

    Mean =   {key: [] for key in names} #Create dict for mean with name keys 
    Median = {key: [] for key in names} #create dict for median with name keys 

    for f in range(len(audio_file)): #loops through each wav in that name
    
        audio = (audio_file[f]) #selects audio
        sound = parselmouth.Sound(audio) #converts it to a sound
        pitch = sound.to_pitch(pitch_floor=75.0, pitch_ceiling=400.0)
        f0 = pitch.selected_array["frequency"] 
        f0 = f0 [f0>0] # Hz (0 for unvoiced)
        pitch_mean = parselmouth.praat.call(pitch, "Get mean", 0, 0, "Hertz") #calculate mean
        pitch_min = parselmouth.praat.call(pitch, "Get minimum", 0, 0, "Hertz", "Parabolic") #min
        pitch_max = parselmouth.praat.call(pitch, "Get maximum", 0, 0, "Hertz", "Parabolic") #max
        pitch_median = float(np.median(f0))

        #write to dictionary 
        #Mean[name].   append(pitch_mean) #write mean to dict for this voice 
        #Median[name]. append(pitch_median) #write median to dict for this voice 

                #write a dictionary 
        dict[f] = {
            "filename": audio,
            "meanPitch": pitch_mean,
            "MedianPitch": pitch_median,
            "MinPitch": pitch_min,
            "MaxPitch": pitch_max,
        }
        print (audio_file)
    return Mean, Median, dict