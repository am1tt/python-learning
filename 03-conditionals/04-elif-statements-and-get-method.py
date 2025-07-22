

## here we will use elif statments to check multiple conditions ## 


name = 'am1t'


if name == 'am1t':
    print("name is am1t")
elif name == 'john':
    print("name is john")
elif name == 'doe':
    print("name is doe")
else:
    print("name is not am1t, john or doe")


## here we are checking multiple conditions using elif statements ##

## if the first condition is true it will execute that block and skip the rest ##

# resulting in printing am1t # 



## ------ ## 

## here we will see how to use the get method with dictionaries ##

## this is more efficient than using if elif statements ## 
name = {
    'am1t':"hello amit sakpal",
    'john':"hello john doe"
}

print(name.get('am1t','this is amit'))
