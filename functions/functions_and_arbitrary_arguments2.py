#exercise 8-13
def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key]=value

    return profile

user_profile = build_profile('obi','amadi',occupation='architect',sex='male',nationality='american')
print(user_profile)