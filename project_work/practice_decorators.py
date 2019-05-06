def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


#@decor (can be used to indicate a function that is
# to be decorated in place of the defining the variable(decorated) that follows.)
def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()