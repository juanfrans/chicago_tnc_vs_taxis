#%% [markdown]
# # Analysis of Transportation Network Companies (TNCs) and Taxis in Chicago
# ## Selecting data to be analyzed
# This notebook takes the downloaded original files and selects one week of data for each dataset. For the TNCs the selected week is November 5 - November 11, 2019. For the taxi trips, the selected week is November 7 - November 13, 2016.
# 
# A project by:<br><br>
# Juan Francisco Saldarriaga<br>
# Senior Data and Design Researcher<br>
# Brown Institute for Media Innovation<br>
# School of Journalism, Columbia University<br>
# jfs2118@columbia.edu<br>
# <br>
# and<br><br>
# David King<br>
# School of Geographical Sciences and Urban Planning<br>
# Faculty Advisor, Barrett Honors College<br>
# Arizona State University<br>
# david.a.king@asu.edu<br>
#
# The original data for this project can be found at:
# * Taxi trips: [Chicago Data Portal](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew), accessed on June 12, 2019.
# * TNC trips: [Chicago Data Portal](https://data.cityofchicago.org/Transportation/Transportation-Network-Providers-Trips/m6dm-c72p), accessed on April 26, 2019.

#%% [markdown]
# **Importing libraries (Pandas and Numpy)**

#%%
import pandas as pd
import numpy as np

#%% [markdown]
# **Setting global paths and filenames**

#%%
inputDataPath = '/Users/juanfrans/Google Drive/08_Brown/1901_ChicagoTNCs/01_Analysis/01_SelectingData/input/'
outputDataPath = '/Users/juanfrans/Google Drive/08_Brown/1901_ChicagoTNCs/01_Analysis/01_SelectingData/output/'
tncInputFileName = 'TNP_Trips.csv'
taxiInputFileName = 'TaxiTrips.csv'
tncOutputFileName = 'SelectedTNC_Trips_181105_181111.csv'
taxiOutputFileName = 'SelectedTaxi_Trips_161107_161113.csv'

#%% [markdown]
# **Loading and exploring TNC data**

#%%
tncData = pd.read_csv(inputDataPath + tncInputFileName, delimiter=',')

#%%
tncData.head()

#%%
tncData.tail()

#%%
tncData.shape

#%%
tncData.dtypes

#%% [markdown]
# **Selecting TNC data for one week (November 5 - November 11, 2018)**

#%%
tncSelectedData = tncData[(tncData['Trip Start Timestamp'] >= '11/05/2018 00:00:00 AM') & (tncData['Trip Start Timestamp'] < '11/12/2018 00:00:00 AM')]

#%%
tncSelectedData.head()

#%%
tncSelectedData.tail()

#%%
tncSelectedData.shape

#%%[markdown]
# **Exporting selected TNC data as a `.csv` file**

#%%
tncSelectedData.to_csv(outputDataPath + tncOutputFileName)

#%% [markdown]
# **Loading and exploring Taxi data**

#%%
taxiData = pd.read_csv(inputDataPath + taxiInputFileName, delimiter=',')

#%%
taxiData.head()

#%%
taxiData.tail()

#%%
taxiData.shape

#%%
taxiData.dtypes

#%%
taxiData['Trip Start Timestamp'].sort_values()

#%% [markdown]
# **Creating new fields of type `datetime` for start and end times**

#%%
# Transform fields to 'Datetime'
taxiData['StartDateTime'] = pd.to_datetime(taxiData['Trip Start Timestamp'])
taxiData['EndDateTime'] = pd.to_datetime(taxiData['Trip End Timestamp'])

#%%
taxiData.dtypes

#%%
taxiData['StartDateTime'].sort_values()

#%% [markdown]
# **Selecting Taxi data for one week (November 7 - November 13, 2016)**

#%%
taxiSelectedData = taxiData[(taxiData['Trip Start Timestamp'] >= '11/07/2016 00:00:00 AM') & (tncData['Trip Start Timestamp'] < '11/14/2016 00:00:00 AM')]

#%%
taxiSelectedData.head()

#%%
taxiSelectedData.tail()

#%%
taxiSelectedData.shape

#%%[markdown]
# **Exporting selected TNC data as a `.csv` file**

#%%
taxiSelectedData.to_csv(outputDataPath + taxiOutputFileName)

#%%
