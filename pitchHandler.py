import parselmouth
from parselmouth.praat import call
import os 



def pitchshift(files, shiftamount, directory_name, parentfolder):  
    for file in files: 
        os.chdir("C:/Users/testarr/Documents/pythoncode/pitch-change/FinalWav")
        sound = parselmouth.Sound (file) #Selects the sound and creates a variable for it 
        #Call a praat command 
        manipulation = call(sound, "To Manipulation", 0.01, 75, 600) #creates a manipulation object
        type(manipulation)
        manipulation.class_name
        pitch_tier = call(manipulation, "Extract pitch tier") #Creates pitch contour 

        call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, shiftamount) 

        call([pitch_tier, manipulation], "Replace pitch tier")
        sound_octave_up = call(manipulation, "Get resynthesis (overlap-add)")
        if not os.path.exists(directory_name): 
            os.mkdir(directory_name) 
        os.chdir(directory_name)
        sound_octave_up.save(f"{'shifted'}{file}", "WAV")

        ... 
    ... 



