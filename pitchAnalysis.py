from storage_handler import write_json

def meanMedian(dict): 
    '''read in the mean and median of each file. checks if there is a significant difference between mean and median'''
    outliers = {} 
    length = len(dict)
    for f in range (length): 
        line = dict[f]
        fmean   = line ['meanPitch']
        fmedian = line ['MedianPitch']
        fname = (line ['filename'])

        fmean = int(float(fmean))
        fmedian=int(float(fmedian))

        percdiff = fmean * .10
        diff = fmean- fmedian
        diff = diff * -1
        if diff > percdiff: 
            outliers [f]= {
            "filename": fname, 
            "meanPitch": fmean, 
            "MedianPitch": fmedian,
            "difference": diff
            }
    
    write_json (outliers)
    ... 

    #Need to see if the mean and median are significantly different 