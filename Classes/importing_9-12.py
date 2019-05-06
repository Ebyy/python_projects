from Admin_class_module import Admin

obi = Admin('obioma','guelph',33)
obi.describe_user()

obi.privileges.show_privileges()

print ("\n...Adding administrator privileges...")

obi.privileges_list = ['can ban user',
                       'can edit video feed',
                       'can moderate discussion forums']

obi.privileges.privileges_list = obi.privileges_list

obi.privileges.show_privileges()