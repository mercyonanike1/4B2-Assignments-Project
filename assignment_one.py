#Get input from user

user_entries = input('Please enter the numbers, separated with space, to get average: ')
if user_entries:
        user_collection = user_entries.split(' ')
        
        total = 0
        for item in user_collection:
            total += float(item)
        avg = total/len(user_collection)
        print('The average of '+ user_entries + ' is ' + str(avg))

elif user_collection != ("1"):
     user_collection == total
            
else:
        print('You did not type anything')

       





























