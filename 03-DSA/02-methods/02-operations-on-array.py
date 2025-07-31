
from array import array


def arrOperations():

    try:

        arr = array('i',[])


        while True:

            print("\n current array : ",arr.tolist())

            print("Choose operation : ")
            print("1. Insert(append)")
            print("2. Remove")
            print("3. pop")
            print("4. Exit")


            choice = input("choice (1-4) : ").strip()

            if choice == '1': 
                val = input("insert element : ").strip()
                indexation = input("at index : ").strip()

                if not val or not indexation:
                    raise ValueError("well cannot add empty value")
                
                val = int(val)
                indexation = int(indexation)

                arr.insert(indexation,val)

                print (f"inserted : {val}")
            
            elif choice == '2':
                val = input("remove element : ").strip()

                if not val: raise ValueError("well Cannot remove empty value")

                val = int(val)

                if val not in arr:
                    raise ValueError(f"{val} is not inside the array")
                
                arr.remove(val)

                print (f"removed : {val}")
            
            elif choice == '3':

                if len(arr) == 0: raise IndexError("cannot pop empty array")

                popped = arr.pop()

                print (f"popped {popped}")
            
            elif choice == '4':

                print("exiting...")
                break 
            else:
                raise ValueError("invalid choice. choose 1-4")
    except ValueError as ve:
        print(f"ValueError : {ve}")
    
    except IndexError as ie: 
        print(f"indexError : {ie}")

    except Exception as e:
        print(f"Exception : {e}")

arrOperations()