names = {
    "am1t":21,
    "john":25,
    "doe":30
}


for i in names:
    print(f"{i} is {names[i]} years old")



for hold in names.keys():
    print(hold)

## we can also use names.keys() to get the keys ## 

## here i is the key of dictionary and names[i] is the value associated with that key # #


teams = {
    "colorado":"rockies",
    "new york":"yankees",
    "boston":"red sox"  
}

for team in teams.values():
    print(team)

## in the above eg we are using values() to get the values of the dictionary ##