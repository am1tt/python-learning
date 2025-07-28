
## some techniques to loop over 


foo1 = dict(am1tt=21 , mop=43)

foo2 = dict(john="44",gen=59)

for i,j in foo1,foo2:
    print(i,j)

## can also use items()

for i in foo1.items():
    print(i)

## using enumerate

for i,j in enumerate([foo1,foo2]):
    print(i,j)

## prints : 0 {am1tt...} , 1 {'john'...}

## using zip 


for i , j in zip(foo1,foo2):
    print(i,j)

## using set() and sorted()

for i  in sorted(set(foo1)):
    print(i,j)