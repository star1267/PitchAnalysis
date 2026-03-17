from pathlib import Path
from typing import Dict
import csv


def write_csv(data):
    """This creates a csv and then write the sentences to that csv"""
    # Opens the csv file to write to it
    path = Path(r".\pitch.csv") #sets path to this csv
    with open(path, "a", newline="") as csvfile: #opens this csv
        fieldnames = ['filename', 'meanPitch', 'MinPitch', 'MaxPitch'] #sets headers 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() #writes headers
        writer.writerows(data.values()) #writes dict data
    ...

