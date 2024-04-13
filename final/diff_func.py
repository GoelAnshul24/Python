import numpy as np


# EXAMPLE 1

# convert list or tuple in numpy arrays
l1 = [2,3,4,5,55,75,354,345,555]
print(type(l1))

# EXAMPLE 2

#using arrange()function
a3 = np.arange(0,20).reshape(4,5)
print(a3)

# EXAMPLE 3 

# using random.randint
#generates random integer ranges fron 0-100
a=np.random.randint(0,100,20)
# Reshape the array to a desired shape, for example, a 4x5 matrix
reshaped_a = a.reshape(4, 5)
# Display the original array and the reshaped array
print("\nOriginal array:")
print(a)
print("\nReshaped array:")
print(reshaped_a)
print(reshaped_a[-1: , -1: ])