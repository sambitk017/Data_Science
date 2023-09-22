"""  We will see here how to aggregate   """
"""   GROUPBY function   """
###  groupby function allows you to group together rows based off a column and perform an aggregate function on them

import numpy as np
import pandas as pd
data = {
    "company": ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    "person": ['sam', 'charlie', 'amy', 'vanessa', 'carl', 'sarah'],
    "sale": [200, 120, 340, 124, 243, 350]
}
list =['a', 'b', 'c', 'd', 'e', 'f']
df = pd.DataFrame(data, index= list)
# print(df)
df_new = df.groupby('company')   #### with the groupby we have use something for aggregation function
# print(df_new.mean())  ### her we are aggregating with the mean function

# print(df.groupby('company').sum().loc['FB'])  ### this is one line code for a group by and sum function on the sale
                                              ### and then returning the value for the index FB
"""   using describe function   """
print(df.groupby('company').describe()) ### this will return the information for the index company and the sales
print(df.groupby('company').describe().transpose())   ### this will return the transposed matrix with company as the columns



