# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:46:40 2020

@author: rzava
"""
import random
import time
import matplotlib.pyplot as plt

#Half the time this doesn't work for random lists (meaning randomly, it doesn't work)
#Finally got it to run with the_nums by running indiv. chunks
def bubble_sort(numbers): # Not the most efficient
    # Answer object 
    answer = numbers.copy()
    # N of numbers in numbers
    n = len(numbers) - 2
    # Index used in the while loop
    i = 0
    # Swap indicator
    swap = True
    # Object to stop the while loop
    notSwap = len(answer) - 2
    while notSwap != 0:   
        if answer[i] > answer[i + 1]: # Compare numbers
            answer[i], answer[i + 1] = answer[i + 1], answer[i] # Swap numbers
            if i == n: # Check index
                i = 0
            else: 
                i += 1            
        else:
            if i == n: # Check index
                i = 0
                notSwap = n
            else: 
                notSwap -= 1
                i += 1
    return answer


def selection_sort(numbers):
    # Answer object 
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]    
    return answer

####    generate lists of numbers    ####
the_nums5 = []
for i in range(0,5):
    n = random.randint(1,100000) #sepcify integers, using large range because of later lengths
    the_nums5.append(n)
    
the_nums50 = []
for i in range(0,50):
    n = random.randint(1,100000)
    the_nums50.append(n)
    
the_nums100 = []
for i in range(0,100):
    n = random.randint(1,100000)
    the_nums100.append(n)
    
the_nums500 = []
for i in range(0,500):
    n = random.randint(1,100000)
    the_nums500.append(n)

the_nums1000 = []
for i in range(0,1000):
    n = random.randint(1,100000)
    the_nums1000.append(n)
    
the_nums5000 = []
for i in range(0,5000):
    n = random.randint(1,100000)
    the_nums5000.append(n)
    
the_nums10000 = []
for i in range(0,10000):
    n = random.randint(1,100000)
    the_nums10000.append(n)

#combine into one list for iterating    
the_nums = [the_nums5, the_nums50, the_nums100, the_nums500, 
            the_nums1000, the_nums5000, the_nums10000]

remember_The_Times = [] #empty list for times
for i in range(0,7):
    start_time = time.time() #specify start time
    selection_sort(the_nums[i]) #run the function for the element
    remember_The_Times.append(time.time() - start_time) 
    #return difference between start and finish into list of times

bubble_Times = []
for i in range(0,7):
    start_time = time.time() #specify start time
    bubble_sort(the_nums[i]) #run the function for the element
    bubble_Times.append(time.time() - start_time)
    #return difference between start and finish into list of times
    
boring_Times = []
for i in range(0,7):
    start_time = time.time() #specify start time
    the_nums[i].sort #run the function for the element
    boring_Times.append(time.time() - start_time)
    #return difference between start and finish into list of times
   
####    Graph    ####
#list of N's    
n = [5, 50, 100, 500, 1000, 5000, 10000]     
#plot the three sets of lists
plt.plot(n, remember_The_Times, 'r-', label = "Selection Sort")
plt.plot(n, bubble_Times, 'b-', label = "Bubble Sort")
plt.plot(n, boring_Times, 'g-', label = "Basic Sorts")
plt.xlim(1, 10000)
plt.ylim(0, 20)
plt.xlabel('N')
plt.ylabel('Time (Seconds)')
plt.legend()
plt.show()
    

