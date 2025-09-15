

def greet(): 
    def message(): 
        print("from inner function")
    message()

greet()

## here a function is inside another function 