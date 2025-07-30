
from array import array 


def appendArray(size):
    arr = array('i',[])
    try:
        for i in range(size): 

            elements = input(f"{i + 1} : ")

            if not elements: raise ValueError("cannot be empty")
            
            elements = int(elements)

            if elements <= 0: raise ValueError("cannot be negative")
            
            arr.append(elements)
            
    except ValueError as ve:
        print("Caught : ",ve)
        raise 

    return arr


try:
    user_size = (input("enter size : ")).strip()

    if not user_size: raise ValueError("input cannot be empty")
    
    user_size = int(user_size)

    if user_size <= 0: raise ValueError("size must me postive")
    
    res = appendArray(user_size)

    print(res)

except ValueError as ve:
    raise None
    
