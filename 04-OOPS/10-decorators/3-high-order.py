

def add(x,y): 
    return x + y 

def subtract(x,y): 
    return x-y

def apply_op(x,y,op): 
    return op(x,y)


res = apply_op(3,5,add)

print(res)


## apply op is high order function that takes 2 function as arg and return the outcomes 
