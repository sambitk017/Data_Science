"""  In this code section we will look into the pandas library  """
"""  Series  """

import numpy as np
import pandas as pd
# labels = ['a', 'b', 'c']
# my_data = [10, 20, 30]
# arr = np.array(my_data)
# d = {'a':10, 'b':20, 'c':30}
#
# data = pd.Series(my_data)
# print(data)  ### by default it gives you the index from 0-n , but you can change by using index
#
# data_1 = pd.Series(my_data, index= labels)     ### this will provide the index as the labels that is initialized above
# print(data_1)


""" Grabing index from the series  """
# ser1 = pd.Series([1, 2, 3, 4], ['usa', 'germany', 'ussr', 'japan'])
# print(ser1['usa'])
#
# ser2 = pd.Series([1, 2, 5, 4], ['Usa', 'Germany', 'Issr', 'japan'])
# print(ser2)


"""  directly providing an array  """
# ser3 = pd.Series(np.zeros(12))
# print(ser3)


"""  adding the series  """
# ser1 = pd.Series([1, 2, 3, 4], index =['usa', 'germany', 'ussr', 'japan'])
# ser2 = pd.Series([1, 2, 5, 4], index =['usa', 'germany', 'Italy', 'japan'])
# ser3 = ser1 + ser2
# print(ser3)    #### it will add the both series on the labels , like both have usa at 1 , so the usa will be 2 after adding

"""   DATA FRAMES   """
# from numpy.random import randn
# np.random.seed(101)
#
# df = pd.DataFrame(randn(5,4), ['a','b','c','d', 'e'], ['w', 'x', 'y', 'z'])
# print(df)

"""  indexing in data frames  """
# from numpy.random import randn
# np.random.seed(101)
#
# df = pd.DataFrame(randn(5,4), ['a','b','c','d', 'e'], ['w', 'x', 'y', 'z'])
# # print(df)
#
# df_1 = df['w']
# print(df_1)
#
# df_2 = df[['x', 'y']]      ### if you want more series in then pass a list of the colums
# print(df_2)


"""  DROPPING A ROW IN DATAFRAME  """
from numpy.random import randn
np.random.seed(101)

# df = pd.DataFrame(randn(5,4), ['a','b','c','d', 'e'], ['w', 'x', 'y', 'z'])   ### in this rows and columns are specified
# df_1 = pd.DataFrame(randn(5,4))     #### In this the rows and columns are not specified
# print(df)
# df['new'] = df['w'] + df['y']
# print(df)
#
# print(df.drop('new', axis=1))  ## remove a colums , axis = 1 is for the columsn
# print(df.drop('a', axis=0))   ## removes a row, axis=0 is for the rows

"""   INDEXING ROWS  """

# row = df.loc['a']   ### this is using the row nmame
# print(row)
#
# row1 = df.iloc[2]   ### this is using the index number of the row that you want
# print(row1)
#
# print(df.loc['b', 'y'])   ### to grab a particular value in the data frame
# print(df.loc[['a', 'b'], ['w', 'y']])  ### to grab a subset from df , give  a list of rows and colums


"""  CONDITIONAL SELECTION using bracket notations  """

# bool_df = df < 0   ### this will return thre boolean value for all the elements where the values are <0
# print(bool_df)

# print(df[bool_df])   #### it will return only the values where it is true or else it will return nan or null
#
# sel = df['w'] > 0                        #####   SINGLE CONDITION #####
# print(df[sel])   ### this will only return the rows will the true values     ####   IMPORTANT #####


# print(df[(df['w']>0) & (df['y']>1)])   ### this will return the output with multiple condition
# """ here & represents the and operator and | (pipe) sign represents the OR operator"""
# print(df[(df['w']>0) | (df['y']>1)])


# reset = df.reset_index()   ### this will change the index into a column and create a index(separate)
# print(reset)
#
# new_ind = "ca ny wy or co".split()
# df["states"] = new_ind
# new_df = df.set_index("states")         ### this will explain that if you have a column , you can set that as the index
# print(new_df)

