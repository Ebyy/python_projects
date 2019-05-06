unconfirmed_users = ['adam','brenda','jen','pam']
confirmed_users = []

#verify and move to confirm
while unconfirmed_users:
     current_user = unconfirmed_users.pop()

     print ("Verifying user " + current_user.title() + " ...")
     confirmed_users.append(current_user)

#to display the confirmed users
print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print (confirmed_user.title())

pets = ['dog','monkey','goldfish','cat','dog','cat','dog']

print (pets)

#To entirely remove a reoccurring word from a list use 'while' loop
while 'dog' in pets:
    pets.remove('dog')

print (pets)