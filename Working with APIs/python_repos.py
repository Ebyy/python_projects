import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
print(repo_dicts)

# Examine the first repository.
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Now let's pull values for some of the keys
print("\nSelected information about first repository:")
print("Name:", repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])

print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
