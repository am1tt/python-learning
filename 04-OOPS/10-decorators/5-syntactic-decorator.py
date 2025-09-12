

def decorator(func): 
    def wrapper(): 
        print("Before Function call")
        func()
        print("After function call")
    return wrapper


@decorator
def foo(): 
    print("foo")

foo()


## hides the decorator logic
