


def shout(text): 
    return text.upper()

def whisper(text):
    return text.lower()


def foo(func): 
    f = func("am1t here")
    print(f)


foo(shout)

foo(whisper)