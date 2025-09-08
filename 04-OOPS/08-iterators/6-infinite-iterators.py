

import itertools

counter = itertools.count(1)


for num in counter: 
    print(num)

    if num == 5: 
        break


## tl;dr : itertools generate infinite values , here i printed till 5 and then used conditional to break it once it reached there  