

counter = 0

def increment(): 
    global counter
    counter += 1


increment()


print(f"val : {counter}")

## note : a global scope | variable is always outside the function 

## here global counter , keyword global is used to refer to outside func counter 

