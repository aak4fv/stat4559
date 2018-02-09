###
### 2017 CitiBike data
### Amy Kim
###

import pandas as pd
import numpy as np
import os
os.chdir("C:\\Users\\amykim0504\\Documents\\Capital Bikeshare Project\\2017 CitiBike")

import glob
filelist2 = glob.glob('*.csv') ## 'glob' searches for csv.files

df2 = pd.DataFrame()
for f in filelist2:
    newdf = pd.read_csv(f)
    newdf.columns = ['duration (s)','start time','stop time','sstation ID','start station',
                     'sstation lat','sstation long','estation ID','end station','estation lat',
                     'estation long','bike ID','user type', 'birth year', 'gender']
    newdf['month'] = (f[8:9]) # adds the month 
    df2 = pd.concat([df2,newdf])

# reads in the csv files for each of the months in 2017 as one dataframe


