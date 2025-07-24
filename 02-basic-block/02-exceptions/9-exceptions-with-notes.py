

try:
    raise TypeError('bad type')
except TypeError as t:
    t.add_note("add some information")
    t.add_note('more informaiton')
    raise 


## same raise format , were we raised typeError execption 

## then added the notes for the exception and then raised it 