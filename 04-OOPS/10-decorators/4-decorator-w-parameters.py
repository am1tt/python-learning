
def decorator(func): 
    def wrapper(): 
        print("pre call")
    func() 
    print("post call")
    return wrapper

def foo(): 
    print("hello")

foo = decorator(foo)

foo()