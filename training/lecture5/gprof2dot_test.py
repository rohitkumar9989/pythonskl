#!/usr/bin/python3

#python3 -m cProfile -o output.pstats gprof2dot_test.py
#../../gprof2dot-2017.9.19/gprof2dot.py -f pstats output.pstats | dot -Tpng -o output.png

def my_func():
    a = [1] *(10**7)
    b = [2] *(2**3**1)
    del b
    return a

if __name__ == '__main__':
    my_func()
