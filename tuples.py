"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable).
Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values.
We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
Unlike list, tuple has few methods.
"""

# syntx
tpl = ('item1', 'item2','item3')

#Length
len(tpl)

# Accessing tuple items Positive
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[0]
second_item = tpl[1]
last_index = len(tpl) - 1
last_item = tpl[last_index]

# Accessing tuple items Negative
"""
Negative indexing means beginning from the end, -1 refers to the last item and the negative 
of the list/tuple length refers to the first item.
"""
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]


# Slicing tuple Positive
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

# Slicing tuple Negative
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

# 'Modify'
"""
Tuple is immutable if we want to modify a tuple we should change it to a list.
"""
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
lst[0] = 'itemModify'
print(lst)
tpl = tuple(lst)
print(tpl)


# Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

# Join
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# Delete
tpl1 = ('item1', 'item2', 'item3')
del tpl1