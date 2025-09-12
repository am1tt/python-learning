


def decorate(func): 
    def wrapper(): 
        "wrapper w doctstr"
        print("pre call")
        func() 
        print("post call")
    return wrapper


@decorate
def foo(): 
    print("foo")

print(foo.__name__)
print(foo.__doc__)
## attribs are used for debugging every function has it btw 

