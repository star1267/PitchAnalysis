import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Index
import dataframe_image as dfi


#// TODO rewrite this in a way that makes more sense 

def plotmeans(dict): 

    names = ["Bella", "River", "Clancy", "Matt" ] #Name of the three voices we are using 
    Gibstdmean   = [[],[],[],[]]
    Gibmean   = [[],[],[],[]]
    Gibmedian = [[],[],[],[]]
    Gibstdmedian= [[],[],[],[]]
    Ieeemean = [[],[],[],[]]
    Ieeemedian  = [[],[],[],[]]
    Ieeestdmean  = [[],[],[],[]]
    Ieeestdmedian  = [[],[],[],[]]

    GibMeanSpeaker    = [[],[],[],[]]
    GibMedianSpeaker  = [[],[],[],[]]
    IeeeMeanSpeaker   = [[],[],[],[]]
    IeeeMedianSpeaker = [[],[],[],[]]

    for n in range(len(names)): #loops through the different speakers names
        for line in dict: #Loops through each row of the dictionary 
                fmean   = int(float(line['meanPitch'])) #extract mean F0 value
                fmedian = int(float(line ['MedianPitch'])) #extract median F0 
                fname = (line ['filename']) #extract file name 

                if "Gib" in fname: #checks if its a gibberish file 
                    if names[n] in fname: #checks if this file is the current name
                        GibMeanSpeaker[n].append (fmean) #creates variable of all the F0 means for this speaker 
                        GibMedianSpeaker[n].append(fmedian)#creates variable of all the F0 medians for this speaker 
                        ... 
                elif "IEEE" in fname: #checks if its an ieee file 
                    if names[n] in fname: #checks if this file is the current name
                        IeeeMeanSpeaker[n].append (fmean) #stores mean 
                        IeeeMedianSpeaker[n].append(fmedian) #stores median
                        ... 
        ...              
        Gibmean[n] = round(np.mean(GibMeanSpeaker[n]), 2) #average mean F0 for this voice 
        Ieeemean[n]= round(np.mean(IeeeMeanSpeaker[n]), 2) #average mean F0 for this voice 
        Gibstdmean[n] = round(np.std(GibMeanSpeaker[n]), 2) #std 
        Ieeestdmean[n]= round(np.std(IeeeMeanSpeaker[n]), 2)#std

        Gibmedian[n] = round(np.mean(GibMedianSpeaker[n]), 2)
        Ieeemedian[n]= round(np.mean(IeeeMedianSpeaker[n]), 2)
        Gibstdmedian[n] = round(np.std(GibMedianSpeaker[n]), 2)
        Ieeestdmedian[n]= round(np.std(IeeeMedianSpeaker[n]), 2)

    fig= plt.figure 
    plt.subplot(1, 2, 1)
    plot( Gibmean,Gibstdmean, Ieeemean, Ieeestdmean, names ,"Mean F0") 
    plt.show

    plt.subplot(1, 2, 2)
    plot(Gibmedian,Gibstdmedian, Ieeemedian, Ieeestdmedian, names, "Median F0" )
    plt.savefig('Plot.png')


    

    table = { 'Name': [names[0], names[1], names[2], names[3]], 
    'Giberish Mean': [Gibmean[0], Gibmean[1], Gibmean[2], Gibmean[3]],
    'Giberish Median': [Gibmedian[0], Gibmedian[1], Gibmedian[2], Gibmedian[3]], 
    'Giberish Std mean':  [Gibstdmean[0], Gibstdmean[1], Gibstdmean[2], Gibstdmean[3]], 
    'IEEE Mean ': [Ieeemean[0], Ieeemean[1], Ieeemean[2], Ieeemean[3]], 
     'IEEE Median': [Ieeemedian[0], Ieeemedian[1], Ieeemedian[2], Ieeemedian[3]],  
     'IEEE Std Mean':  [Ieeestdmean[0], Ieeestdmean[1], Ieeestdmean[2], Ieeestdmean[3]],
     }

    df = pd.DataFrame(table)

    dfi.export(df, 'Table.png')
    return (fig)









def plot (Gibdata, Gibstd, Ieeedata, Ieeestd,names, Title): 
    x = [1,2,3,4]
    plt.plot(x,Gibdata, color="r")
    plt.errorbar(x, Gibdata, yerr=Gibstd, fmt="o", color="r")
    plt.plot(x,Ieeedata, color="b")
    plt.errorbar(x, Ieeedata, yerr=Ieeestd, fmt="o", color="b")
    plt.xlabel("Speaker")
    plt. ylim (80, 240)
    plt.title(Title)
    plt.xticks(x, names)
    plt.legend(['Gibberish', 'IEEE']) 
    ... 

    