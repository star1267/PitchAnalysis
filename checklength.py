import librosa
import numpy as np


def checklength (GibFiles, IEEEFiles): 
    def calculate (Files): 
        names = list(Files.keys())
        durations = []
        for name in names: 
            for i in range(720): 
                file = Files[name][i]
                audio_data, sample_rate = librosa.load(file)
                duration= librosa.get_duration(y=audio_data, sr=sample_rate)
                durations.append(duration)
            maximum = max(durations)
            minimum = min(durations)
            print(f"Duration: {file}_{duration:.2f} seconds")
        return (durations, maximum, minimum )
    GibLength, GibMax, GibMin= calculate (GibFiles)
    IEEELength, IEEEMax, IEEEMin= calculate (IEEEFiles)

    print("IEEE Max" , IEEEMax, "Gib Min", GibMin )


























    ... 