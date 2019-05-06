unconfirmed_users = ['alice','brian','chad','jen']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print ("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nDone")
print ("Find the list of confirmed users below")
print (confirmed_users)
