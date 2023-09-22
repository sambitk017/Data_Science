"""   here we will see how to combine data frames trough variety of methods  """
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'A':['A0', 'A1', 'A2', 'A3'],
    'B':['B0', 'B1', 'B2', 'B3'],
    'C':['C0', 'C1', 'C2', 'C3'],
    'D':['D0', 'D1', 'D2', 'D3'],
}, index=[0, 1, 2, 3])



df2 = pd.DataFrame({
    'A':['A4', 'A5', 'A6', 'A7'],
    'B':['B4', 'B5', 'B6', 'B7'],
    'C':['C4', 'C5', 'C6', 'C7'],
    'D':['D4', 'D5', 'D6', 'D7'],
}, index=[4, 5, 6, 7])


df3 = pd.DataFrame({
    'A':['A8', 'A9', 'A10', 'A11'],
    'B':['B8', 'B9', 'B10', 'B11'],
    'C':['C8', 'C9', 'C10', 'C11'],
    'D':['D8', 'D9', 'D10', 'D11'],
}, index=[8, 9, 10, 11])

# print(df1)
# print(df2)
# print(df3)

"""   CONCATINATION   """  ### caoncatination basically glues together the data frames

# df = pd.concat([df1, df2, df3])
# print(df)
#
# df_new = pd.concat([df1, df2, df3], axis=1)   ### this will join the dataframes over the columns
# print(df_new)


"""   MERGING   """

left = pd.DataFrame({
    'key':['k0','k1','k2','k3'],
    'A':['a0','a1','a2','a3'],
    'b':['b0','b1','b2','b3']
})

right = pd.DataFrame({
    'key':['k0','k1','k2','k3'],
    'C':['c0','c1','c2','c3'],
    'D':['d0','d1','d2','d3']
})

df = pd.merge(left, right, how='inner', on='key')   ### syntax for merging the data frames on the key columns
print(df)


"""   JOINING   """
""" helps in combining the columns of two potentially differently index data frames """
# df_1 = left.join(right, how='inner', on='key') ##### this is the syntax
# print(df_1)
