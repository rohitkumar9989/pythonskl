#!/usr/bin/python3
#python3 -m memory_profiler profile_test.py 

# mprof run profile_test.py 
# mprof plot

@profile
def my_func():
    a = [1] *(10**7)
    b = [2] *(2**3**1)
    del b
    return a

if __name__ == '__main__':
    my_func()
