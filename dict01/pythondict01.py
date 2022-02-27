#!/usr/bin/env python3

# Create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

#Display parts of the disctionary
print(switch['hostname'])
print(switch['ip'])

# Request a 'fake' key
# print( switch['lynx'] ) # Be sure to comment out th                          #is line, or your program w                          #ill continue to fail! If a                          #key is requested that does                          #not exist, an error will b                          #e thrown!
# Request a 'fake' key with .get() method
print('\nfirst test - .get():')
print(switch.get('lynx', 'THE KEY IS IN ANOTHER CASTLE!'))
print('\nThird test - .get():')
print(switch.get('version'))

print('\nFourth test - .keys():')
print(switch.keys())

print('\nFifth test - .values():')
print(switch.values())

print( "\nSixth test - .pop():")
switch.pop('version') # Removes this key and value pair
print(switch.keys()) # Notice the value of version is gone

print('\nSeventh test - ADD a new value: \n')
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())


print('\nEigth test - ADD a new value: \n')
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())
