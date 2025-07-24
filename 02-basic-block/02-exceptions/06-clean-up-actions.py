
## user-defined exceptions

## defining clean-up actions # #

try:
    raise KeyboardInterrupt
finally:
    print('user-defined : exception')
    raise