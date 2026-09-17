# LISTS

empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0


web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
print('Web technologies:', web_techs)

lst = ['Barco', 2500, True, {'country':'Saturn', 'city':'Saturnaria'}] # list containing different data types
print(type(lst[0]))
print(type(lst[1]))
print(type(lst[2]))
print(type(lst[3]))


fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)


fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
print(fruits[0] is fruits[-len(fruits)])
print(fruits[1] is fruits[-len(fruits) + 1])


# Unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic) # 'Denmark','Finland','Norway','Iceland'
print(es)


# Slicing

"""
Positive Indexing: 
We can specify a range of positive indexes by specifying the start, end and step, the return value will
be a new list.
default values:
 * start = 0
 * end = len(lst) - 1 (last item)
 * step = 1
"""
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
all_countries = countries[0:4] # it returns all the countries
# this will also give the same result as the one above
all_countries = countries[0:] # if we don't set where to stop it takes all the rest
france_and_belgium = countries[1:3] # it does not include the first index and the index value 3
fr_be_sw_de_fi_no_ic_es = countries[1:]
fr_sw_fin_ice = countries[::2] # here we used a 3rd argument, step. It will take every 2cnd item

"""
Negative Indexing:
We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
"""
all_countries = countries[-4:] # it returns all the fruits
norway_and_iceland = countries[-3:-1] # it does not include the last index
all_from_norway_reverse = countries[-3:] # this will give starting from -3 to the end
reverse_countries = countries[::-1] # a negative step will take the list in reverse order


# Modifiying lists
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries[0] = 'Chequia'
print(countries)       #  ['Chequia', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries[1] = 'Italy'
print(countries)       #  ['Chequia', 'Italy','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
last_index = len(countries) - 1
countries[last_index] = 'Netherlands'
print(countries)        #  ['Chequia', 'Italy','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Netherlands']


# Checking Items in a List
does_exist = 'Spain' in countries
print(does_exist)  # False
does_exist = 'Netherlands' in countries
print(does_exist)  # True


# Adding Items to a List
"""
# syntax
lst = list()
lst.append(item)
"""

countries.append('Andorra')
print(countries)           # ['Chequia', 'Italy','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Netherlands', 'Andorra']
countries
countries.append('Bulgaria')   # ['Chequia', 'Italy','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Netherlands', 'Andorra', 'Bulgaria']
print(countries)


# Insert items
"""
to insert a single item at a specified index in a list
"""
countries.insert(3, 'Greece')
print(countries)
countries.insert(6, 'Spain')
print(countries)


# Remove
countries.remove('Spain')
countries.remove('Greece')
print(countries)


# Pop (like remove)
"""
removes the specified index, (or the last item if index is not specified)
"""
countries.pop()
print(countries)
countries.pop(0)
print(countries)


# Del
"""
removes the specified index and it can also be used to delete items within index range.
It can also delete the list completely
"""
del countries[0]
print(countries)
del countries[1]
print(countries)
del countries[1:3]
print(countries)
del countries
#print(countries) # This should give: NameError: name 'countries' is not defined


# Clear
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries.clear()
print(countries)


# Copy
"""
It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1.
Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1.
But there are lots of case in which we do not like to modify the original instead we like to have a 
different copy. One of way of avoiding the problem above is using copy().
"""

countries_copy = countries.copy()
print(countries)


# Join
"""
seprador.join(lst)
"""
positive_numbers = [1, 2, 3, 4, 5]
numbers_join = '-'.join(str(positive_numbers))
print(numbers_join)

"""
'+' 
"""
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

"""
'extend()'
"""
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
lst = [0, *lst_one, *lst_two]
print(lst)
lst = [0].extend(lst_two) # lst_zero = [0]
lst_two.extend(lst_one)
print(lst_one)


# Count
"""
returns the number of times an item appears in a list
"""
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3


# Index
"""
returns the index(first occurrence) of an item in the list
"""
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence


# Reverse
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]


# Sort
"""
can use sort() method or sorted() built-in functions. The sort() method reorders
the list items in ascending order and modifies the original list. If an argument
of sort() method reverse is equal to true, it will arrange the list in descending order.
"""
# sort(): this method modifies the original list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries.sort() # sort in alphabetical order
print(countries)
countries.sort(reverse=True)
print(countries)

numbers = [1,4,2,8,0]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# sorted(): returns the ordered list without modifying the original list
print(sorted(countries))
countries = sorted(countries, reverse=True)
print(countries)