

## get square 

def getSquare(x):
    try:
        if not isinstance(x,(int,float)):
            raise TypeError("input must be a number")
        if x < 0:
            raise ValueError("square must not be defined for negative numbers")
        
        
        res = x * x
        return res
        
    except ValueError as e:
        e.add_note("custom note for valueError and getSquare")
        print(f"error in square function : {e}")
        raise
    


while True:
    try:
        user_input_str = input("enter number : ")
        
        if not user_input_str.strip():
            print("input cannot be empty")
            continue 
        
        num = int(user_input_str)
        
        res = getSquare(num)
        
        print("result : ",res)
        break
    except ValueError as e:
        print(f"invalid input : {e}")
    except TypeError as te:
        print(f"Type error: {te}")
    except Exception as ee: 
        print(f"An unexpected error occurred: {ee}")

## i wrote this to utilize what i learned in exceptions whilst also learning about 

## covered : 
# 1 : exception handling(raises,blocks) , 2 : parameterized func , 3 : returning func , isistances 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
