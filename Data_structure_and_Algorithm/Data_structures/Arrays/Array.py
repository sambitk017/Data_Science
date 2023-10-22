
# from array import *
#
# # 1. Creating an array.
#
# temp_array = array('i',[3,5,7,8,9])
#
# for i in temp_array:
#     print(i)
#
#
# # 2. Accessing elements through indexes
# print("Step 2")
# print(temp_array[3])
#
# # 3. Appending value to the array using append() method
#
# print("Step 3")
# temp_array.append(6)
# print(temp_array)
#
# # 4. Inserting value in array using insert().
# print("Step 4")
# temp_array.insert(3, 11)
# print(temp_array)
#
#
# # 5. Extending the  python array using extend() method
# print("Step 5")
# temp_array1 = array('i', [10,11,12])
# temp_array.extend(temp_array1)
# print(temp_array)
#
# # 6. Add items from list into array using fromlist() method in the existing array
# print("Step 6")
# tempList = [20,21,22]
# temp_array.fromlist(tempList)
# print(temp_array)
#
# # 7. Remove any array element using remove().
# print("Step 7")
# temp_array.remove(11)
# print(temp_array)
#
# # 8. Remove last array element using pop() method from the array
# print("Step 8")
# temp_array.pop()
# print(temp_array)
#
# # 9. Fetch any element through its index using index() method
# print("Step 9")
# print(temp_array.index(21))
#
# # 10. Reverse a python array using reverse() method
# print("Step 10")
# temp_array.reverse()
# print(temp_array)
#
# # 11. Get array buffer information through buffer_info() method
# print("Step 11")
# print(temp_array.buffer_info())
#
# # 12. Check for number of occurrences of an element using count() method
# print("Step 12")
# temp_array.append(11)
# print(temp_array.count(11))
# print(temp_array)
#
# # 13. Convert array to a python list with same elements using tolist() method
# print("Step 14")
# print(temp_array.tolist())
#
# # 14. Slice Elements from an array
# print("Step 16")
# print(temp_array[2:])



#######################################################################################################################
#######################################################################################################################

import numpy as np

twoD_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoD_array)

newtwoD_array = np.insert(twoD_array, 1, [[1,2,3,4]], axis=0)
print(newtwoD_array)

print(len(twoD_array))

newtwoD_array = np.append(twoD_array, [[1,2,3,4]], axis=0)
print(newtwoD_array)
print(len(newtwoD_array))    # Returns the total number of rows
print(len(newtwoD_array[0])) # Returns the total number of columns


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newtwoD_array, 1, 2)
print("Heloooooooooooooooooo")
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoD_array)


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


print(searchTDArray(twoD_array, 444))

newTDArray = np.delete(twoD_array, 1, axis=1)
print(newTDArray)