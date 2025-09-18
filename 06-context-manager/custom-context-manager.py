

import contextlib

@contextlib.contextmanager


def context_manager(num): 
    print('enter')
    yield 1 
    print('exit')


with context_manager(2) as cm:
    print('right in the iddle with cm = {}'.format(cm))