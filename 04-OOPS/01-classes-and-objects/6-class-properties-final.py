

class scale:
 
    def __init__(self,key):
        self._key = key

    def get_key(self): 
        return self._key
    

    def set_key(self,your_key): 
        if not your_key.strip():
            print("cannot be empty")
        else:
            self._key = your_key
        
    def del_key(self):
        print("deleting the key")
        del self._key
    

    key = property(get_key,set_key,del_key)


    def __str__(self): 
        return f"default key : (name={getattr(self,'_key','DELETED')})"


instrument1 = scale("G# major")

print(instrument1)


new_instrument = input("want to change the key ? , enter new : ")

instrument1 = new_instrument

print(instrument1)
