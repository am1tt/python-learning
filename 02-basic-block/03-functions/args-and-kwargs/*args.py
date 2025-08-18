
## 2 types of arguements , keyword and non keyword 

## non-keyword refers to *args


def mult(*container):
    result = 1

    for number in container:
        result *= number
    return result



print(mult(2,3))

print(mult(4,5,6))

## the above code , collects arguements into tuple

## allowing me to handle multiple values without specifying it 
