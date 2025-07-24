
## here handling multiple exceptions 


def foo():
    exc = [OSError('foo1') , SystemError('FOO2')]
    raise ExceptionGroup('multiple exceptions found : ',exc)

try:
    foo()
except Exception as e:print(f'caught {type(e)}')

