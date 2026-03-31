import matplotlib.pyplot as plt
import numpy as np

#// TODO rewrite this in a way that makes more sense 

def plotmeans(dict): 

    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 
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
        print (n)
        Gibmean[n] = np.mean(GibMeanSpeaker[n]) #average mean F0 for this voice 
        Ieeemean[n]= np.mean(IeeeMeanSpeaker[n]) #average mean F0 for this voice 
        Gibstdmean[n] = np.std(GibMeanSpeaker[n]) #std 
        Ieeestdmean[n]= np.std(IeeeMeanSpeaker[n])#std

        Gibmedian[n] = np.mean(GibMedianSpeaker[n])
        Ieeemedian[n]= np.mean(IeeeMedianSpeaker[n])
        Gibstdmedian[n] = np.std(GibMedianSpeaker[n])
        Ieeestdmedian[n]= np.std(IeeeMedianSpeaker[n])

    fig= plt.figure 
    plt.subplot(1, 2, 1)
    plot( Gibmean,Gibstdmean, Ieeemean, Ieeestdmean, names ,"Mean F0") 
    plt.show

    plt.subplot(1, 2, 2)
    plot(Gibmedian,Gibstdmedian, Ieeemedian, Ieeestdmedian, names, "Median F0" )
    print ()
    return (fig)

def plot (Gibdata, Gibstd, Ieeedata, Ieeestd,names, Title): 
    x = [1,2,3,4]
    plt.plot(x,Gibdata, color="r")
    plt.errorbar(x, Gibdata, yerr=Gibstd, fmt="o", color="r")
    plt.plot(x,Ieeedata, color="b")
    plt.errorbar(x, Ieeedata, yerr=Ieeestd, fmt="o", color="b")
    plt.xlabel("Speaker")
    plt.title(Title)
    plt.xticks(x, names)
    plt.legend(['Gibberish', 'IEEE']) 
    ... 

    