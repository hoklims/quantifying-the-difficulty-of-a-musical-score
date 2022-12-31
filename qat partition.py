# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:39:01 2022

@author: Hokli
"""

"""quantifying the difficulty of a partition such as a children's canteen"""

# 3/4 time signature
import statistics
# Import the mean function from the statistics module
from statistics import mean

def reform(partition):
    """Convert 5 to 1, 4 to 2, 3 to 3, 2 to 4, 1 to 5, don't touch 0"""
    """Save format ([])"""
    reform_list = []
    # Iterate through each sublist in the partition
    for i in range(len(partition)):
        # Initialize an empty sublist in the reform_list
        reform_list.append([])
        # Iterate through each element in the sublist
        for j in range(len(partition[i])):
            # Convert the element according to the specified rules and append to the reform_list
            if partition[i][j] == 5:
                reform_list[i].append(1)
            elif partition[i][j] == 4:
                reform_list[i].append(2)
            elif partition[i][j] == 3:
                reform_list[i].append(3)
            elif partition[i][j] == 2:
                reform_list[i].append(4)
            elif partition[i][j] == 1:
                reform_list[i].append(5)
            else:
                reform_list[i].append(0)
    # Return the reformatted partition
    return reform_list

def variance_partition(partition):
    variance_list = []
    # Iterate through each sublist in the partition
    for i in range(len(partition)):
        # Calculate the variance of the sublist and append to the variance_list
        variance = statistics.variance(partition[i])
        variance_list.append(variance)
    # Return the list of variances
    return variance_list

def algo_diff(partition):
    """Calculate the difficulty of a partition"""
    
    diff_list = []
    # Iterate through each sublist in the partition
    for i in range(len(partition)):
        difficulty = 0
        # Iterate through each element in the sublist, except for the last element
        for j in range(len(partition[i])-1):
            # If the next element is not 0, add the absolute difference between the current element and the next element to the difficulty
            if partition[i][j+1] != 0:
                difficulty += abs(partition[i][j] - partition[i][j+1])
        # Append the difficulty of the sublist to the diff_list
        diff_list.append(difficulty)
    # Return the list of difficulties
    return diff_list

def algo_diff_sync(partition_right, partition_left):
    """Calculate the difficulty of a synchronised partition"""
    
    diff_list = []
    # Iterate through each sublist in the right partition
    for i in range(len(partition_right)):
        difficulty = 0
        # Iterate through each element in the sublist
        for j in range(len(partition_right[i])):
            # If the element in the right partition is not 0, add the absolute difference between the element in the right partition and the corresponding element in the left partition to the difficulty
            if partition_right[i][j] != 0:
                difficulty += abs(partition_right[i][j] - partition_left[i][j])
        # Append the difficulty of the sublist to the diff_list
        diff_list.append(difficulty)
    # Return the list of difficulties
    return diff_list

def diff_similitude(partition):
    """Calculate the difficulty of a partition similitude"""
        
    finger_list = []
    # Iterate through each sublist in the partition
    for i in range(len(partition)):
        # Iterate through each element in the sublist
        for j in range(len(partition[i])):
               # If the element is not 0, append it to the finger_list
               if partition[i][j] != 0:
                    finger_list.append(partition[i][j])
        # Remove duplicate elements from the finger_list
        finger_list = list(set(finger_list))
    # Return the finger_list
    return finger_list

def diff_similitude_mesure(variance_right, variance_left):
    # Return a measure of difficulty based on the variances of the right and left partitions
    if variance_right < 1 and variance_left < 1:
        return 1
    elif variance_right >= 1 and variance_right <= 2 and variance_left >= 1 and variance_left <= 2:
        return 2
    elif variance_right > 2 and variance_left > 2:
        return 3    
    
    
# Initialize some example partitions
Danse_villageoise_1 = ([3,1,3], [5,3,5], [4,3,2], [3,0,1],[3,1,3],[5,3,5],[4,3,2],[1,0,0])
Danse_villageoise_2 = ([5,0,1], [5,0,0], [1,0,0], [5,3,1], [5,0,1],[5,0,0],[1,0,0],[5,0,0])
# Reformat the second partition
Danse_villageoise_2_R = tuple(reform(Danse_villageoise_2))

# Calculate the difficulty of the synchronised partition
sync_diff = algo_diff_sync(Danse_villageoise_1, Danse_villageoise_2_R)
# Calculate the average difficulty of the synchronised partition
sync_diff_avg = sum(sync_diff) / len(sync_diff)

# Calculate the difficulty of the right and left partitions
test_1 = algo_diff(Danse_villageoise_1)
test_2 = algo_diff(Danse_villageoise_2)

# Calculate the mean variance of the right and left partitions
variance_list_right = mean(variance_partition(Danse_villageoise_1))
variance_list_left = mean(variance_partition(Danse_villageoise_2))

# Calculate the overall difficulty of the right and left partitions
diff_right = (sum(test_1) / len(test_1)) + variance_list_right
diff_left = (sum(test_2) / len(test_2)) + variance_list_left

# Print the difficulty of the right, left, and synchronised partitions
print("right " + str(diff_right))
print("left " + str(diff_left))
print("together " + str(diff_right + diff_left + sync_diff_avg))