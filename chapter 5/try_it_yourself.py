from hashlib import new


current_users = ['user1','user2','user3','user4','user5']
new_users = ['new1','new2','new3','user4','user5']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is already being used")
    else:
        print(f"{new_user} is available")
