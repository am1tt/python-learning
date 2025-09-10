

def read_numbers(): 
    for i in range(5): 
        yield i
    

def square(numbers): 
    for num in numbers: 
        yield num * num 

for sq in square(read_numbers()): 
    print(sq)

## i yield returns the param to the square and then it reques to the sq
