

# Q : if languages of two friends are same what will happen to the program in problem 6 ## 

# the code is same from 06 ,as they refer to same question # 

def returnValuesandKeys(size):
    container = dict()

    try:
        for i in range(size):

            add_keys = input(f"names of friends  {i + 1} : ").strip()


            if not add_keys:
                raise ValueError("name cannot be empty")                        

            add_values = input(f"enter their favrioute language  : ").strip()



            if not add_values:
                raise ValueError("language cannot be empty")
            
                        
            ## here solution ## 

            if add_values in container.values():
                print(f"{add_keys} liks the same language : {add_values}")


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


## added the condition to check the same language used values here ##

## solved : am1tt ## 