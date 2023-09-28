""" NUMPY """
""" Numpy is a linear algebra library for python"""

"""  np.array  """  ## This numpy arrays work with 2 types  1. 1D vectors , 2. 2D matrices

import numpy as np
# my_list =[1, 2, 3]
# arr = np.array(my_list)     ## this is converting a list into an 1D array
# print(arr)
# print(my_list)
#
# my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     ## thuis is converting a nested list into a matrix or 2D matrix
# mat = np.array(my_mat)
# print(mat)

"""  np.arrange  """  ## acts as the range()
# arr = np.arange(1, 10, 2)    ## here 2 is the step size
# print(arr)


"""  np.linspace  """   ##takes a third argument for number of points you want between your range
# arrr = np.linspace(0, 5, 10)  ## this will return a 1D array with equally spaced intervals from 1 to 5
# print(arrr)


"""   using random to create arrays """

# print(np.random.rand(5))   ## this will return a 1D array for random 5 numbers b/w o-1
#
# print(np.random.randint(1, 100))   ## to return any int randomly , but by giving the number argument we can get multiple numbers


"""  using np.reshape  """   ## this is to create a data frame / to reshape the 1D array ##
# arr = np.arange(25)        ## this will return array from 0-24
# print(arr)
# mat = arr.reshape(5, 5)    ## this will reshap that 1D array into 5x5 matrix
# print(mat)

"""  NUMPY INDEXING and SELECTION """
"""   indexing 1D array   """
# arr = np.arange(0, 11)
# print(arr)
# ind = arr[0:5]   ## slicing in arrays are just the same as the lists
# print(ind)

"""  indexing 2D array"""
# arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# print(arr_2d)
# print(arr_2d[0][0])  ## this will give you the number 5  1st [] for row , 2nd [] for the column else , you can put together
# print(arr_2d[0,2])          ##same as above
#
# print(arr_2d[1:,:2])    ## this return the sliced part of the matrix , 1st slice operator is for the row, 2nd is for column
# print(arr_2d[1:])


"""  Conditional selection  """
# arr = np.arange(1, 11)
# bool_arr = arr > 5    ## taking And array putting a comparision operator on it gives boolean array
# print(arr[bool_arr])

# arr = np.arange(0,51)
# even_arr = arr%2==0    ## this will return the values from 0-51 with the arr which are even
# print(arr[even_arr])

arr = np.arange(0,9).reshape(3, 3)
print(arr)