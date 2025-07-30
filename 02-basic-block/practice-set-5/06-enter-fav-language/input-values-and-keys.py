

# create an empty dictionary allow 4 friends to enter their favrouite language as values 
# and use keys as their names , assume that the names are unique # 


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


## i utlized here ## 

# Exceptions handlings , Raises , 
# Returning parameterized functions 
# input validations
## solved : am1tt ## 