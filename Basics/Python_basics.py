"""
This file will give us basics of the python
"""

""" Using .format in scripts """
# we use this input the parameter inside the print statements eg:-

# name = "sambit"
# age = 21
# print('my name is {one}, my age is {two}'.format(one=name, two= age))


""" But a better way to do it is using f-string. EG:-"""
# name =  input("enter name:- ")
# age = int(input("enter age:- "))
# print(f"my name is {name}, my age is {age}")


""" NESTED LIST  """
# my_list = [1, 2, [3, 4]]
# print(my_list[2])  ## to ge the index 2 (list containing 3,4)
# print(my_list[2][1])  ## to get the value 4 from the list
#
# nest = [1, 2, 3, [4, 5, ['target']]]
# print(nest[3][2][0])  ## to get the "target" from the list


"""  NESTED DICTIONARIES  """
# d ={'key1' : 'value', 'key2' : "123"}
# print(d['key2'])  ## to get the values 123 , we here use the key instead of index number
#
# e = {'k1' : [1, 2, 3]}
# print(e['k1'][1])  ## to get the value 2 from the list inside the dict
#
# f = {'k1' : {'inner_key' : [1, 2, 3, 4]}}
# print(f['k1']['inner_key'][3])  ## to get the 4 in the list


"""  TUPLES  """
""" the only difference b/w list and tuples are that tuples can not re-assign values """
# t = (1, 2, 3, 4)
# print(t[1])
# t[1] = 5
# print(t) ## this will return error


"""  LIST COMPREHENSION  """
"""  it is writing the for loop in the reverse order  """
# x = [1, 2, 3, 4]
# out = []
# for num in x:
#     out.append(num**2)
# print(out)
# ## OR ##
# out = [num**2 for num in x]  ## this code will run the same above code but in one line


"""  MAP  """
"""  MAP :- we use this functions to apply a function to other item in a list or say anything """

# def times2(var):
#     return var*2
#
# seq = [1, 2, 3, 4] ## now we want map that func above on that list , so it will return a list with
# print(list(map(times2, seq)))                   ## times2 of every element in the seq

## to avoid writing this function we use lamda function, to rewrite the def times2.
""" A BRIEF 
    def times2(var):
    return var*2 

    this can be written as 

    def times2(var):return var*2

    AND lamda function removes the words that are not required 
    there removing def, return, times2
    we are left with 

    var : var*2

    now just add lamda infront
    i.e lamda var : var*2"""  ## this is a lamda expression

## so instead of writing function and passing that in the map function we can
## directly write the lamda expression in the map statement
# seq = [1, 2, 3, 4]
# print(list(map(lambda num: num*2, seq)))


"""  FILTER  """
""" FILTER :- filter outs the elements from a sequence"""
"""  filter only works with lamda on when the lambda is use take out the boolean value"""

# seq = [1, 2, 3, 4, 5, 6]
# print(list(filter(lambda num : num%2 ==0 , seq)))


"""  TUPLES UNPACKING  """

# x = [(1, 2), (3, 4), (5, 6)]
# for item in x:
#     print(item)
#
# ## OR ##
#
# for (a, b) in x:
#     print(a)

