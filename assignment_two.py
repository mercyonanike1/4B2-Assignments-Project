#Write a program that takes in multiple data and returns a dictionary. 
# Note: The value should be one value for one key and number should be integer. A key without 
# a value, ask the user for the key and also the number used should be an integer.

 #####ANSWER###
 
#To input users entry
user_entries = input('Please enter key:value to get dictionary: ')
#To check if user actually typed in something
if user_entries:
    user_collection = user_entries.split(' ')
    user_dict = {}
    for item in user_collection:
        key_value = item.split(':')
        #Check if all keys has its individual values. Split to get the value item
        if len(key_value) != 2 or not len(key_value[1]):
            response = input('Would you like to enter a value for key ' + str(key_value[0]) + ': ')
            #To convert the users input to snmall letter
            if response and response.lower() == 'yes':
                value = input('Please enter a value for key ' + str(key_value[0]) + ': ')
                user_dict[key_value[0]] = value
        else:
            user_dict[key_value[0]] = key_value[1]

print(user_dict)