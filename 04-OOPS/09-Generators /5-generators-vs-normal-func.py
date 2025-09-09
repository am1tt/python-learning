

## gen func 

def generate_numbers():
    yield 1
    yield 2
    yield 3 




def normal_numbers(): 
    return [1,2,3]


for n in generate_numbers(): 
    print(n)

for n in normal_numbers():
    print(n)

## as said previously yield are generative , and also are returning