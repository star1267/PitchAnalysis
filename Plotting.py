import matplotlib.pyplot as plt
import numpy as np



def plotmeans(dict): 
    #// TODO I think this can be changed into a for loop?? 

    GibBella = [] 
    GibClancy= []
    GibMatt  = []
    GibRiver = []

    IeeeBella = []
    IeeeClancy= []
    IeeeMatt  = []
    IeeeRiver = []
    
    
    for line in dict: 
            fmean   = line ['meanPitch']
            fmedian = line ['MedianPitch']
            fname = (line ['filename'])
            fmean = int(float(fmean))
            fmedian=int(float(fmedian))


            if "Gib" in fname: 
                if "Bella" in fname: 
                    GibBella.append (fmean)
                elif "Clancy" in fname: 
                    GibClancy.append (fmean)
                elif "Matt" in fname: 
                    GibMatt.append (fmean)
                elif "River" in fname: 
                    GibRiver.append (fmean)

            elif "IEEE" in fname: 
                if "Bella" in fname: 
                    IeeeBella.append (fmean)
                elif "Clancy" in fname: 
                    IeeeClancy.append (fmean)
                elif "Matt" in fname: 
                    IeeeMatt.append (fmean)
                elif "River" in fname: 
                    IeeeRiver.append (fmean)

    plt.figure
    plot (GibBella,GibClancy, GibMatt , GibRiver, "Gibberish Means" )
    plt.figure
    plot (IeeeBella,IeeeClancy, IeeeMatt , IeeeRiver, "IEEE Means" )

    ... 

def plot (Bella, Clancy, Matt, River, Title): 
    x = 1,2,3,4 
    GibelPlot= np.mean(Bella)
    GibmattPlot= np.mean(Matt)
    GibclancyPlot= np.mean(Clancy)
    GibriverPlot= np.mean(River)
    

    GibelSD= np.std(Bella)
    GibmattSD= np.std(Matt)
    GibclancySd= np.std(Clancy)
    GibriverSd= np.std(River)

    y = GibelPlot, GibmattPlot, GibclancyPlot, GibriverPlot
    eer =  GibelSD, GibmattSD, GibclancySd, GibriverSd

    plt.bar(x,y)
    plt.errorbar(x, y, yerr=eer, fmt="o", color="r")
    plt.title(Title)
    plt.show()
    ... 