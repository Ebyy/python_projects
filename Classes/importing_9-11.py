import User_module

administrator = User_module.Admin('obi onuendo','calgary',32)
administrator.describe_user()

administrator.read_attempts()

administrator.privileges.show_privileges()

administrator.privileges_list = ['can block user','can reset password','can add user']

administrator.privileges.privileges_list = administrator.privileges_list

print ("\n....Adding Privileges....")

administrator.privileges.show_privileges()