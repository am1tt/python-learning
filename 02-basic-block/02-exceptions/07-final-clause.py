
## from clean-up actions 

## using final clause 


def divide(x,y):
    try:
        res = x / y
    except ZeroDivisionError:print("Division by zero")
    else:
        print("result : ",res)
    finally:
        print("final clause exec")
    

divide(2,7)