import numpy as np

# Aggregrate function = summarize data and return ouput in one line 

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]]) 

print(np.sum(array)) # It will give the total sum 
print(np.min(array)) # reutrns the minimum value 
print(np.max(array)) # returns the maximum value 
print(np.mean(array)) # returns the mean 
print(np.std(array)) # reutrns the standard deviation
print(np.argmin(array)) # return the 
print(np.argmax(array)) # return the index of the maximum value within an arra
print(np.var(array)) # reutrns the variance 
