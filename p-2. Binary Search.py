#Step 1
# Given an array of integers nums which
# is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

#Step 2
# def search(list,query):
# input[1,2,3,4,5,6,7],4 output: 3
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
#Edge Cases
# The query number is in first element of the list.
# The query number is in the last element of the list.
# The list is empty.
# The list contain duplicate elements.
# The query number is not in the list.

#step3.
#

#Step3
# starting position of the index number is 0
# while the list in not empty loop through
# Check if the index number is equal to the postion
# increment the postion
# if not check if the list is finished.
# Return -1 if not found

def search(list,query):
    position = 0;
    while True:
        if list[position] == query:
            return position
        position+=1
        if len(list) == position:
            return -1

test = {
    'input':{
        'list': [3,4,5,6],
        'query': 6
    },
    'output': 3
}
print(search(**test['input']))

#TimeComplexcity: n
