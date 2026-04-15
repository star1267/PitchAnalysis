import librosa
import numpy as np


def checklength (GibFiles, IEEEFiles): 
    def calculate (Files): 
        names = list(Files.keys())
        durations = []
        files = []
        for name in names: 
            for i in range(len(Files[name])): 
                file = Files[name][i]
                audio_data, sample_rate = librosa.load(file)
                duration= librosa.get_duration(y=audio_data, sr=sample_rate)
                durations.append(duration)
                files.append(file)
                if 'Gib' in file: 
                    if duration < 4.90: 
                        print(f"Duration: {file}_{duration:.2f} seconds")
                elif 'IEEE' in file:
                    if duration > 5: 
                        print(f"Duration: {file}_{duration:.2f} seconds")
            maximum = max(durations)
            minimum = min(durations)
        return (durations, maximum, minimum )
    GibLength, GibMax, GibMin= calculate (GibFiles)
    IEEELength, IEEEMax, IEEEMin= calculate (IEEEFiles)

    print("IEEE Max" , IEEEMax, "Gib Min", GibMin )

    ... 