my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]# this line copies the list into a new list

#this doesn't work:
#friends_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)