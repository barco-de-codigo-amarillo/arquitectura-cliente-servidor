# sytnx
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

# while - else
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


# break and continue I
# Break: We use break when we like to get out of or stop the loop.
"""
while condition:
    code goes here
    if another_condition:
        break
"""

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue: With the continue statement we can skip the current iteration, and continue with the next
"""
while condition:
    code goes here
    if another_condition:
        continue
"""
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1



# For loop on list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# For loop on string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# For loop on tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary: gives you the key of the dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# For loop on sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and continue II
# break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# The Range function
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]