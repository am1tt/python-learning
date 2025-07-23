

## here we will use range to iterate through a squence of numbers ## 

for i in range(1,10):
    print(i)


## here we will use reversed to reverse the range of numbes ##

for i in reversed(range(1,10,2)):
    print(i)

## 2 here skips every second number in the range ## 


for i in range(1,21):
    if i == 2:
        continue
    print(i)