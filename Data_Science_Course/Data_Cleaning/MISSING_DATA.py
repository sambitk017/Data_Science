"""   Here we will learn to manage the missing values   """
import numpy as np
import pandas as pd

"""   DROPPING MISSING VALUES   """
d = { 'A':[1, 2, np.nan] , 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}
df = pd.DataFrame(d)
# print(df)

"""   DROPNA method """  ### use to drop any row with any single or multiple nan values. we can specify axis to check
#                         ###  for row or column
# df_1 = df.dropna(axis=1)
# print(df_1)
#
# df_2 = df.dropna(thresh=2)   #### thresh is use to give the minimum number of non-NA values along the row or colum
# print(df_2)


"""   FILLING MISSING VALUES  """
print(df)

""" FILLNA method  """
df_new = df.fillna(value= 2)   ### this will fill in the missing values in the whole data dframe with the values 2
# print(df_new)

"""  filling missing values in particular columns """
df_mod = df['A'].fillna(value=df['A'].mean())  ### this line will fill the missing values in the B column with the mean
print(df_mod)                                                ### values of the column