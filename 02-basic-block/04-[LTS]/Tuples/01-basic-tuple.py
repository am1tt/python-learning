

foo = (10,34,"am1tt",4)


print(foo)

## mapping it in loop

for i in foo:
    print([i])

## indexing

print(foo[1])


## slicing it 

print(foo[1:])

## combining tuple

new_tuple = (23,55,"mop")

combined_tuple = new_tuple + foo


print(combined_tuple)