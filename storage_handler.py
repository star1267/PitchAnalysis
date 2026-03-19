from pathlib import Path
import csv
import os.path

def check_csv (fname): 
    #check that file doesnt exist
    if not os.path.exists(fname): 
        return None
    else: 
    #if file does exist just print that it exists
        print ("CSV already exists. Content appended to bottom of document")
    ... 

def write_csv(data, fname):
    """This creates a csv and then write the sentences to that csv"""
    # Opens the csv file to write to it
    check_csv(fname)
    path = Path(fname) #sets path to this csv
    with open(path, "a", newline="") as csvfile: #opens this csv
        fieldnames = ['filename','MedianPitch', 'meanPitch', 'MinPitch', 'MaxPitch'] #sets headers 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() #writes headers
        writer.writerows(data.values()) #writes dict data
    ...

