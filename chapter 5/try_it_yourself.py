usernames = ['name1','name2','name3','name4','admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
         print(f"Hello {username}, thank you for logging in")
