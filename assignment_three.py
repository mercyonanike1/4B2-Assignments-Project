# Write a program that takes in numebrs and returns the second largest.

user_entries = input('Please enter values to find second largest: ')
if user_entries:
        user_collection = user_entries.split(' ')
        user_collection.remove(max(user_collection))
        print('Second largest value is ' + str(max(user_collection)))
else:
        print('Invalid entries')

    