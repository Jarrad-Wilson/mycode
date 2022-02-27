#!/usr/bin/env python3

# Create a list called list1
list1 = ['cisco_nxos', 'artista_eos', 'cisco_ios']

print(list1) # Display list1

# Print the second item in the list
print(list1[1])

# Add second list, then combine list1 and lis2
list2 = ['juniper']
list1.extend(list2)

# Print results 
print(list1)

# Create list3 and append it to list1

list3 = ['10.1.0.1', '10.2.0.1', '10.3.0.1']
list1.append(list3)

# Print the results
print(list1)

# Print element 5 in list1
print(list1[4])

animals = ['dog', 'cat', 'rat', 'cow']
print(animals)
