import numpy as np
import pandas as pd

sal = pd.read_csv("Salaries.csv")
# print(sal)
# print(sal.info)
# print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])     ### this is like where statement in SQL
# print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])

print(sal.loc[0])
