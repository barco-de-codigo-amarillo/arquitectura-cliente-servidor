"""
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson.
The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and
un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find 
he union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
"""

# syntx
st = {'item1', 'item2', 'item3', 'item4'}

# len() method
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

# Accessing items in Set
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

# Add
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

# Add multiple items: update()
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

# Remove
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# Pop
"""
remove a random item from a list and it returns the removed item
"""
st = {'item1', 'item2', 'item3', 'item4'}
st.pop()  # removes a random item from the set

# Clear
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# Delete (del)
st = {'item1', 'item2', 'item3', 'item4'}
del st

# Discard
st.discard('item5') # si no está no produce error

# Converting list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

# Joining sets

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1


# Finding intersection items: .intersection()
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon


# Checking the subset and the super set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False


# Difference
"""
returns the difference between two sets or using - symbol
"""
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

# Symmetric Difference: se elimina lo que es común a los dos conjuntos
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon

# Disjoint
"""
two sets do not have a common item or items
"""
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}