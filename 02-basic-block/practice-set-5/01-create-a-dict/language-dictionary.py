

## Question : Write a program to create a dictionary of hindi words with values as their 
# english transalation provide user with an option to look it up ! 

dictionary = {
    "namaste": "hello",
    "paani": "water",
    "kitab": "book",
    "ghar": "home",
    "dost": "friend"
}

words = """
    "namaste"
    "paani"
    "kitab"
    "ghar"
    "dost
"""

print(f"""    word list
      {words}
      """)

user_input = input("choose : ").strip().lower()

if user_input in dictionary:
    print(f"english transalation : {dictionary[user_input]}")
else:
    print("translation was not found")

## solved : am1tt 