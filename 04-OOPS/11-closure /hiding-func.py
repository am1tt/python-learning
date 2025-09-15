

def multiplier(fact): 
    def multiply(number): 
        return number * fact
    return multiply



double = multiplier(2)

result = double(5)


print(f"result : {result}")