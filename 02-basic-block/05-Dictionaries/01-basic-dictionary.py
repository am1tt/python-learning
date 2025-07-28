
## consist of key values and pairs

foo = {'am1tt' : 21 , 'john1' : 34}

print(foo)


## mapping through dictionary ## 

for i in foo:
    print([i])

## adding ing dictionary ## 

foo['mop'] = 86 

print(foo)

## deleting in dictionary ## 

del foo['mop']

print(foo)


## sorting out the dict

sorted(foo)

print(foo)


## checking pairs with boolean responses # 

print('am1tt' in foo) #true
print('mop' in foo) ## obviously its false as i removed it using del 