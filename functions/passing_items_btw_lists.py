#moving an item from list to list can be done in different ways

unprinted_designs = ['iphone case','robot pendant','dodecahedrone']
completed_models = []
"""
Simulate printing each design until none left
"""
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print ("Printing: " + current_design)
    completed_models.append(current_design)

print ("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)