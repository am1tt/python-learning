
## Raising exceptions


try:
    raise NameError("error : invalid arguement") # this is the exception error
except NameError: # if namError here in try block and raising it incase it flew 
    print("exception flew : ") #this exec first btw 
    raise


## basically raise , raises or singals an error , can be valueERror or type as well 