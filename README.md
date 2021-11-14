# EPAi4.0 Session 6
Github Proile : [harshb-15](https://github.com/harshb-15)
## Scopes and Closure
This assignment lets us play with scopes of objects and making a closure of them. 
It has 4 parts :

1. Docstring Length Checker
2. Next Fibonacci Number Generator
3. Function Counter
4. Modified Function Counter

## Part - 1
### Docstring Length Checker
```
def check_ds(fn, *args):
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
```
This Function takes a function and it's arguments as input and outputs it if the docstring of that function is more than 50 characters.
It will raise `ValueError` if the inputs are not correct.
The logic is to check the length of `fn.__doc__` .
## Part - 2
### Next Fibonacci Number Generator
```
def next_fib(n):
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
```
This function will return the next fibonacci number to the one provided.
It will raise `ValueError` if the input is not in the series and if the input itself is not an integer. Logic is to create fibonacci numbers in a loop till you find the one provided, store the previous two numbers and then return the addition.
## Part - 3
### Function Counter
```
def new_fn_counter(fn, *args):
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
```
This function counts the number of times a function was called and stores it in a global dictionary. It will raise `ValueError` if the inputs are not provided correctly like not providing a function(or wrong one), giving extra arguments.

The logic is to access the elements of dictionary accroding to the function and raising the value of that by one. As this function's main motive is to count the number of function is called, any vaalue in the dictionary should not be negative and hence will give a `Warning` if it is.
## Part - 4
### Modified Function Counter
```
def mod_new_fn_counter(fn, d, *args):
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
```
This function works exactly same as our previous Function Counter Function but here a dictionary can be passed to keep a check of function in a separate dictionary instead of a global one.

### How to run the file
1. `pyTest` is needed to run the `test_session6.py`, so `pip install pytest` will do the job. 
2. Clone all files to your local repository.
3. Open a terminal in that repository and type in `python -m pytest test_session6.py` and press enter.