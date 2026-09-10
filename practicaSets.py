# The difference between the following data types: string, list, tuple and set
"""
1. String (str)What it is: A sequence of characters used to store text.Key Feature: It is immutable.
2. List (list): What it is: An ordered, collection of items of any data type [30 Days of Python].Key Feature: It is highly 
flexible and mutable.
3. Tuple (tuple)What it is: An ordered collection just like a list, but completely immutable [30 Days of Python].
Key Feature: Once created, you cannot add, remove, or change any of its elements.
4. Set (set)What it is: An unordered collection of distinct (unique) items [30 Days of Python].Key Feature: It automatically
removes duplicates
"""

# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Using the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
lst = sentence.split(' ')
st = set(lst)
print(len(st))
print(st)


# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
st_age = set(age)
len_age = len(age)
len_st_age = len(st_age)
print(len_age, len_st_age)