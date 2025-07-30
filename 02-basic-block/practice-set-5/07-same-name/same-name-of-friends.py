

# if the names of 2 friends are same , what will to the program in problem 6 # 

# the code is same from 06 ,as they refer to same question # 

def returnValuesandKeys(size):
    container = dict()

    try:
        for i in range(size):

            add_keys = input(f"names of friends  {i + 1} : ").strip()


            if not add_keys:
                raise ValueError("name cannot be empty")                        
            
            if add_keys in container:
                raise ValueError("cannot add duplicate friend")

            add_values = input(f"enter their favrioute language  : ").strip()


            if not add_values:
                raise ValueError("language cannot be empty")


            container[add_keys] = add_values

        return container 
    
    except ValueError:
        print(f"invalid input")
        return None

            
    


try:
    user_size = int(input(f"enter size : "))

    result = returnValuesandKeys(user_size)

    print(result)
except ValueError:
    print("Invalid or empty input")


## added the raise and condition for duplicate friend ## 
## solved : am1tt ## 