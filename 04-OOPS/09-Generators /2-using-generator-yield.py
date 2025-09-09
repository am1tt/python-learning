

def count_up_to_three(): 
    yield 1
    yield 2
    yield 3


counter = count_up_to_three()

for num in counter:
    print(num)

## basically with help of method and yeild we created generator 

## this is effiecient and does not store in memory 

