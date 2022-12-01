# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Step1
# To find the bad verisons from the list of n versions and return the bad version staring point



#Step2
# input[1,2,3,4,5,6] bad=4 output[4]
# Edge Case
# The bad version in not in list
# The list may have duplicate
# The bad version is in start of the list
# The bad version in in end of the list

# #step3 & 4

def isbadVerion(version,bad):
# starting postion of the list is 0
    position = 0
# loop through the list until empty
    while position<version:
        # check if the  of the list is the targeted bad version
        if



# if not, increment the postion
# check if the list is finish looping
# return -1 if it is finish

