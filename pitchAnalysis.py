
from storage_handler import write_json
def meanMedian(dict): 
    outliers = {} 
    length = len(dict)
    for f in range (length): 
        line = dict[f]
        fmean   = line ['meanPitch']
        fmedian = line ['MedianPitch']
        fname = (line ['filename'])

        fmean = int(float(fmean))
        fmedian=int(float(fmedian))

        diff = fmean- fmedian
        diff = diff * -1
        if diff > 10: 
            outliers [f]= {
            "filename": fname, 
            "meanPitch": fmean, 
            "MedianPitch": fmedian,
            "difference": diff
            }
    
    write_json (outliers)
    ... 

    #Need to see if the mean and median are significantly different 