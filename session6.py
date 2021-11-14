from typing import Type


def check_ds(fn, *args):
    '''It checks whether the provided function has a docstring of minimum 50 characters'''
    if(str(type(fn)) != "<class 'function'>"):
        raise TypeError("Input Function only")
    if len(args) > 0:
        raise ValueError("Unwanted Arguments given")

    def inner(*args):
        nonlocal fn
        l = len(fn.__doc__)
        if l >= 50:
            return fn(*args)
        else:
            return "Your function does not have at least 50 charecters in your docstring"
    return inner


def next_fib(n):
    '''It will check if the provided number is already in the fibonacci series and if it is it will output the next number to it'''
    if not isinstance(n, int):
        raise TypeError("Enter an Integer")

    def inner():
        nonlocal n
        if n == 0 or n == 1:
            return 1
        else:
            f1 = 1
            f2 = 2
            while(True):
                if n == f2:
                    return f1+f2
                f3 = f1+f2
                f1 = f2
                f2 = f3
                if(f2 > n):
                    return "Enter a valid number which is in the fibonacci sequence"
    return inner


d = {"add": -2, "mul": 0, "div": 0}


def add(a, b):
    return a+b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def new_fn_counter(fn, *args):
    '''This will update a global dictionary which will keep hold of counts of different function called'''
    if(str(type(fn)) != "<class 'function'>"):
        raise TypeError("Input Function only")
    if len(args) > 0:
        raise ValueError("Unwanted Arguments given")
    def inner(*args):
        nonlocal fn
        global d
        bl=True
        for ct in d.values():
            if ct<0:
                bl=False
                break
        if fn == add:
            d["add"] += 1
        elif fn == mul:
            d["mul"] += 1
        elif fn == div:
            d["div"] += 1
        else:
            raise ValueError("Function not in dictionary")
        if bl == False:
            raise Warning("Count should not be negative")
        return fn(*args)
    return inner


d1 = {"add": 1, "mul": 3, "div": 4}


def mod_new_fn_counter(fn, d, *args):
    '''This s similar to new_fn_counter but instead of a global dictionary, any dictionary provided can be updated'''
    if(str(type(fn)) != "<class 'function'>"):
        raise TypeError("Input Function and Dictionary only")
    if(str(type(d)) != "<class 'dict'>"):
        raise TypeError("Input Function and Dictionary only")
    if len(args) > 0:
        raise ValueError("Unwanted Arguments given")
    bl = True
    for ct in d.values():
        if ct < 0:
            bl = False
            break
    def inner(*args):
        nonlocal fn
        nonlocal d
        if fn == add:
            d["add"] += 1
        elif fn == mul:
            d["mul"] += 1
        elif fn == div:
            d["div"] += 1
        else:
            raise ValueError("Function not in dictionary")
        if bl == False:
            raise Warning("Count should not be negative")
        return fn(*args)
    return inner



