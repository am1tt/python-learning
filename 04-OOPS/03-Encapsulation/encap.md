
### Encapsulation
* Encapsulation in python means , basically binding (attributes) and methods (functions) together inside a class , and restricting direct access to some parts of it 

### Why encapsulation ? 
* Data Protection --> Precents accidental changes from outside 
* control --> you decide how attributes are acessed modified / (via methods)
* flexibilty --> you can change internal logic later , without breaking the code 


### How to do encap ? 

self.name --> public (accessed anywhere)

`_name` --> protected (should not be accessed directly,but can be)

`__name` --> private (harder to access from outside)

## Encap is implemented through access modifiers 
--

can be `public` , `protected` ,`private`