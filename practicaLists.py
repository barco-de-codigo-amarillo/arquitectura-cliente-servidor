# Declare an empty list
lst = list()

# Declare a list with more than 5 items
countries = ['Spain', 'Denmark', 'Iceland', 'Netherlands', 'France']

# Find the length of your list
print(len(countries))

# Get the first item, the middle item and the last item of the list
first_item = countries[0]
middle_item = countries[abs(len(countries) // 2)]
last_item = countries[len(countries) - 1]
print(first_item + ' ' + middle_item + ' ' + last_item)

# Declare a list variable named it_companies and assign initial 
# values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
it_companies[0] = 'Meta'
print(it_companies)


# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first_item = it_companies[0]
middle_item = it_companies[abs(len(it_companies) // 2)]
last_item = it_companies[len(it_companies) - 1]
print(first_item + ' ' + middle_item + ' ' + last_item)

# Print the list after modifying one of the companies
it_companies[4] = 'Linux'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('NVidea')

# Insert an IT company to it_companies
it_companies.insert(4, 'Anthropic')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2].upper()

# Join the it_companies with a string '#;  '
it_companies_join = '#; '.join(it_companies)

# Check if a certain company exists in the it_companies list
does_exist = 'IBM' in it_companies

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies_reverse = it_companies.sort(reverse=True)

# Slice out the first 3 companies from the list
first_3_companies = it_companies[0:3]

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]

# Slice out the middle IT company or companies from the list
middle_index = (len(it_companies) // 2) + 1
middle_it_company = it_companies[middle_index]

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
del it_companies[(len(it_companies) // 2) + 1]
print(it_companies)

# Remove the last IT company from the list
del it_companies[len(it_companies) - 1]

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

# After joining the lists copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = front_end
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
