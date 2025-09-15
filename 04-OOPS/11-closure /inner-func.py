

def outer_func(): 
    outer_var = "val" 

    def inner_func(): 
        print(outer_func)
    


    return inner_func

## here the inner-func uses the outer_var variable
