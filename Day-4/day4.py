# Multiprocessing

# import time
# import multiprocessing 


# def cal_squares(numbers):
#     for n in numbers:
#         time.sleep(3)
#         print("Squares: " + str(n*n))

# def cal_cubes(numbers):
#     for n in numbers:
#         time.sleep(3)
#         print("Cubes: " + str(n*n*n))



# if __name__ == "__main__":
#     arr = [2,3,4,5]
#     p1 = multiprocessing.Process(target=cal_squares, args= (arr,))
#     p2 = multiprocessing.Process(target=cal_cubes, args= (arr,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Done!")

# Multiprocessing queue 
# import multiprocessing 
# q = multiprocessing.queue() 

# -- Lives in shared memory 
# -- used to share data between processes

# Queue module:
# import queue 
# q = queue.Queue()

# -- Lives un im-process memory 
# -- Used to share data between threads


# Lock in python 

# Why do we need lock in real life ?

'''Without lock, multiple threads might try to update counter at the same time, 
 leading to incorrect results. Using Lock ensures only one thread modifies the 
 shared data at a time.'''


'''When to Use
Use Lock in:
Banking systems (balance updates)
File writing
Shared memory updates
Any multi-threaded program that modifies shared resources '''
 


# Multiprocessing pool 

# map : 
# The map() function is used to apply a function to every item in an iterable 
# (like a list) and return a new iterable (usually a map object) with the results.

# Why Use map()?
# Cleaner than a for loop
# Faster for large datasets (internal optimization)
# Good for applying the same function to each element of an iterable


# Main Purpose of reduce()
# The reduce() function is used to apply a function cumulatively 
# to the items of an iterable, reducing it to a single value.


# Why Use reduce()?
# To collapse a list into a single result.
# Makes code shorter and more functional-style.

# Often used in:
# Summing numbers
# Multiplying numbers
# Finding min/max
# Joining strings


# Python testing frameworks
# -- Unittest 
# -- Nose 
# -- pytest 


# import mathlib 

# def test_cal_total():
#     total = math.calc_total(4,5)
#     assert total == 9 
# def test_cal_multiply():
#     result = mathlib.test_cal_multiply(10,3)
#     assert result == 30 

# Pytest: Skip / run tests selectively 

# Topics :
# 1. Skip tests 
# 2. selectively run tests uesing their name 
# 3. Custom markers 


#Numpy Introduction :
# Numpy in extremely popular python modules it is heavily used in scientic computing
# 3 Main benefits of numpy array over a python list 
# 1. Less Memory 
# 2. Fast 
# 3. Convinient

# import numpy as np 
# import time 
# import sys 


# size = 1000000 

# l1 = range(size)
# l2 = range(size) 


# a1 = np.arange(size)
# a2 = np.arange(size) 

# #python list 
# start = time.time()
# result = [(x+y) for x,y in zip(l1,l2)]
# print("Numpy took: ", (time.time() - start )* 1000)/


# import numpy as np 

# # Single Demention Array 

# a1 = np.array([1,2,3])
# print(a1.ndim )

# # Multi Demention Array 
# a2 = np.array([[1,2],[3,2],[4,5]], dtype=float)
# print(a2.ndim) 

# print(a2.size)
# print(a2.shape)
# print(a2[0])

# z = np.zeros((3,4))
# print(z)
# o = np.ones((3,4))
# print(o)

# r = np.arange(1,11)
# print(r)

# liner_space = np.linspace(1,5,10)
# print(liner_space) 

# reshape function is used to reshape the array 
# ravel funxtion arrange the items side by side  

# a.min()
# a.max()
# a.sum() 

# axis in x = 1, y = 0 (rows = 1, columns = 0)
 
# a = np.array([[12,10],[5,8]])
# b = np.array([[6,7],[1,3]])

# print(a)
# print(b)
# print(a+b)
# print()
# print(a-b)
# print()
# print(a*b)

# numy : slicing / stacking and indexing with boolean arrays 

# Topics  
# 1. Indexing and slicing 
# 2. Iterating through arrays 
# 3. Stacking together two arrays 
# 4. Indexing with boolean arrays

import numpy as np 

a = np.array([[12,10,15],[5,8,18],[1,2,3]])
b = np.array([[6,7,8],[1,5,3],[3,5,7]])


# for cell in a:
#     print(cell)

# for cell in a.flat:
#     print(cell)
# r = np.vstack((a,b))
# print(r)

# r = np.hstack((a,b))
# print(r)