import numpy as np
import pandas as pd

df = pd.DataFrame({
    'col1':[1, 2, 3, 4],
    'col2':[444,555, 666, 444],
    'col3':['abc', 'def', 'ghi', 'xyz']
})

"""   workin on the operations on data frames   """
# df_1 = df['col2'].unique()  ### returns the unique values in the col2, will return an array
# df_2 = df['col2'].nunique()  ## returns the number of unique values
# df_3 = df['col2'].value_counts()   ### returns how many times the uniques value occured
# print(df_3)


""" Apply method """
# def times2(x):
#    return x*2
# """ to apply this function to any df we can use apply """
# new_df = df['col1'].apply(times2)   #### this will broad cast this function to each element of the specified column
# print(new_df)


"""   sorting the dataframes   """
print(df)
df.sort_values('col2')


"""   PIVOT TABLES   """
df.pivot_table(values='D', index=['A', 'B'], columns=['C'] )