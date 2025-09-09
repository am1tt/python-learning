

def numbers(): 
    yield 1
    yield 2
    yield 3

gen = numbers()


print(next(gen))
print(next(gen))

for num in gen: 
    print(num)

## its simple , the loop continues from where it left and does not re-iterate
