
## using a dict() constructor here 

# directly sequences from the key value pairs 


foo = dict(am1tt="sakpal",mop=22)

foo2 = dict(afja=89,popw=90)

print(foo)

## can mix strings and integers and others datatypes as well btw 


## using zip here to union the dict #

c = dict(zip(foo,foo2))

print(c)

## maping through the dict()

for i in foo2:
    print(i)