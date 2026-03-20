from pathlib import Path
import csv
from csv import DictReader
import json 

def write_csv(data, fname):
    """This creates a csv and then write the sentences to that csv"""
    # Opens the csv file to write to it
    path = Path(fname) #sets path to this csv
    with open(path, "w", newline="") as csvfile: #opens this csv
        fieldnames = ['filename','MedianPitch', 'meanPitch', 'MinPitch', 'MaxPitch'] #sets headers 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() #writes headers
        writer.writerows(data.values()) #writes dict data
    ...

def read_csv(filename): 
    pitchData = {}
    with open(filename, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
    return (list_of_dict) 

def write_json (data):
    json_str = json.dumps(data, indent=4)
    with open("Outliers.json", "w") as output:
        json.dump(data, output,indent=2 )

    ##Write outliers to a json 
    ...
