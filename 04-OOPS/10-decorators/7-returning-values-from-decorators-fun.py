

def doub_result(fill): 
    def wrapper(a,b): 
        result = fill(a,b)
        return result * 2 
    return wrapper

@doub_result
def mult(a,b):
    return a * b

res = mult(4,4)

print("result : ",res)