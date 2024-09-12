import random

target = random.randint(1,9)
print(target)

rand_list=[]
n=9
for i in range(n):
    rand_list.append(random.randint(1,9))

print(rand_list)

rand_list.sort()
print(rand_list)

def find_middle(lst):
    if not lst:  # Check if the list is empty
        return "The list is empty."
 
    length = len(lst)  # Get the length of the list
 
    if length % 2 != 0:  # Check if the length is odd
        middle_index = length // 2
        return lst[middle_index]
 
    # If the length is even
    first_middle_index = length // 2 - 1
    second_middle_index = length // 2
    return (lst[first_middle_index], lst[second_middle_index])

oddResult = find_middle(rand_list)

print(oddResult)

