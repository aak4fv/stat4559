###
### 2017 Capital Bikeshare data
### Amy Kim
###

import pandas as pd
import numpy as np
import os
os.chdir("C:\\Users\\amykim0504\\Documents\\Capital Bikeshare Project\\2017 Cabi Data")

import glob
filelist = glob.glob('*.csv') ## 'glob' searches for csv.files

df = pd.DataFrame()
for f in filelist:
    newdf = pd.read_csv(f)
    newdf.columns = ['duration (ms)','start date','end date','sstation num','start station',
                     'estation num','end station','bike num','member type']
    newdf['quarter'] = (f[5:7]) # adds the quarter 
    df = pd.concat([df,newdf])

# reads in the csv files for each of the 4 quarters in 2017 as one dataframe
# need to standardize member type column
# in Q4, changes from registered to member

df['duration (ms)'].count() 
'3758862 total trips'

np.round(np.average(df['duration (ms)'])/1000,4)
np.round(np.average(df['duration (ms)'])/60000,4) # convert to minutes
'average duration = 1227.4356 seconds = 20.4573 minutes'

rship = df['duration (ms)'].groupby(df['member type']).count()
cas_per = rship[0]/rship.sum()*100
'casual riders = 27.23%'
mem_per = (rship[1]+rship[2])/rship.sum()*100
'member riders = 72.77%'

startst = df['duration (ms)'].groupby(df['start station']).count().sort_values(ascending=False)[0:10]
'''
Columbus Circle / Union Station                          70068
Lincoln Memorial                                         65889
Jefferson Dr & 14th St SW                                59269
Massachusetts Ave & Dupont Circle NW                     46706
15th & P St NW                                           43307
Jefferson Memorial                                       42531
Smithsonian-National Mall / Jefferson Dr & 12th St SW    42414
Henry Bacon Dr & Lincoln Memorial Circle NW              40666
4th St & Madison Dr NW                                   37757
14th & V St NW                                           33161
'''

endst = df['duration (ms)'].groupby(df['end station']).count().sort_values(ascending=False)[0:10]
'''
top 10 end stations 
Columbus Circle / Union Station                          73579
Lincoln Memorial                                         66495
Jefferson Dr & 14th St SW                                61137
Massachusetts Ave & Dupont Circle NW                     50808
15th & P St NW                                           46074
Jefferson Memorial                                       43849
Smithsonian-National Mall / Jefferson Dr & 12th St SW    43848
Henry Bacon Dr & Lincoln Memorial Circle NW              40602
4th St & Madison Dr NW                                   37934
14th & V St NW                                           36237
''' 

topbike = df['duration (ms)'].groupby(df['bike num']).count().sort_values(ascending=False)[0:10]
'''
top 10 bikes used
bike num
W23386    1697
W22897    1644
W23349    1642
W22982    1628
W22530    1601
W23160    1578
W23336    1566
W22517    1562
W23295    1554
W23186    1548
'''

roundtrip = df[df['start station']==df['end station']]
roundtrip['duration (ms)'].count()
'150998 round trips'

'''
could perform further analysis of above variables/metrics based on segmentation 
by quarter (month) and member type
'''

################################################################################

df[df['duration (ms)'] == df['duration (ms)'].max()]
'''
longest trip = 12951459402 ms = approx. 150 days 
--> indicates possible docking problems, another issue for CaBi
'''

df[df['duration (ms)'] > 86400000].count()
'779 trips that lasted more than 24 hours'
df[df['duration (ms)'] > 172800000].count()
'365 trips that lasted more than 48 hours'
df[df['duration (ms)'] > 604800000].count()
'66 trips that lasted more than 168 hours (one week)'

