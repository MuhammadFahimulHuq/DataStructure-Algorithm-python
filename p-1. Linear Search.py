# step1. we need to write a program to find the postion
# of a given number in a list of number arranged in
# decreasing order. We also need to minimize the number
# of times we access elements from the list.

# card[13,11,10,7,4,3,2,1]
# query[0,1,2,3,5,6,7,8,9]


# step2. Inputs[13,11,10,7,4,3,2,1], 7 | outputs[3]
#Edge case
# 1. The number query occurs somewhere in the middle of the list cards
# 2. Query is the first elements in cards.
# 3. Query is the last element in cards.
# 4. The list cards contain just one element, which is query.
# 5. The list cards does not contain number query.
# 6. The list cards is empty.
# 7. The list cards contains repeating numbers.
# 8. The number query occurs at more than one position in cards.

#step3.
#1.Create a variable postion with the value 0
#2.Check whether the number at index position in card equals query.
#3.If it does,position is the answer and can be returned from the function.
#4.If not, increment the value of position by 1, and repeat step 2 to 5 till we reach the last postion.
#5. If the number was not found return -1.

#step4.
def locate_card(cards,query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position+=1
        if position == len(cards):
            return -1
test={
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query':7
    },
    'output':3
}
print(locate_card(test['input']['cards'],test['input']['query']))