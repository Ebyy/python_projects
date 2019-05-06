unprinted_designs = ['iphone case','robot pendant','dodecahedrone']
completed_models = []

def print_models(unprinted_designs,completed_models):
    """
    Simulate printing each design until none left
    Move printed designs to completed list
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print ("Printing model:" + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the midels that were printed"""

#the """fffff ghgdvsh""" can be used to beat the indent when using the def function

    print ("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#every function should have one specific task like above
#the first stage prints each design or shows that they are being printed
#the second function displays the completed models

