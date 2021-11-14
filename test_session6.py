import pytest
import inspect
import os
import math

import session6


# check_ds

def test_session6_check_ds_wrong_input():
    with pytest.raises(TypeError, match=r".*Input Function only*"):
        session6.check_ds('sac')
    with pytest.raises(TypeError, match=r".*Input Function only*"):
        session6.check_ds(1+2j)


def test_session6_check_ds_output():
    def temp1():
        '''This docstring is less than 50 characters'''
        return "works"

    def temp2():
        '''This docstring has more than 50 characters, This docstring has more than 50 characters, This docstring has more than 50 characters'''
        return "works"

    assert session6.check_ds(temp1)(
    ) == "Your function does not have at least 50 charecters in your docstring", "check_ds is not working as expected"
    assert session6.check_ds(
        temp2)() == "works", "check_ds is not working as expected"


def test_session6_check_ds_unwanted_args():
    def temp1():
        '''This docstring is less than 50 characters'''
        return "works"

    def temp2():
        '''This docstring has more than 50 characters, This docstring has more than 50 characters, This docstring has more than 50 characters'''
        return "works"

    with pytest.raises(ValueError, match=r".*Unwanted Arguments given*"):
        session6.check_ds(temp2, temp1)(1, 2)


# next_fib


def test_session6_next_fib_wrong_input():
    with pytest.raises(TypeError, match=r".*Enter an Integer*"):
        session6.next_fib('sac')
    with pytest.raises(TypeError, match=r".*Enter an Integer*"):
        session6.next_fib(1+2j)


def test_session6_next_fib_output():
    assert session6.next_fib(
        13)() == 21, "next_fib function does not work as expected"
    assert session6.next_fib(14)(
    ) == "Enter a valid number which is in the fibonacci sequence", "next_fib function does not work as expected"


# new_fn_counter

def test_session6_new_fn_counter_wrong_input():
    with pytest.raises(TypeError, match=r".*Input Function only*"):
        session6.new_fn_counter('sac')
    with pytest.raises(TypeError, match=r".*Input Function only*"):
        session6.new_fn_counter(1+2j)


def test_session6_new_fn_counter_output():
    session6.d = {"add": 0, "mul": 0, "div": 0}
    temp_add = session6.new_fn_counter(session6.add)
    temp_mul = session6.new_fn_counter(session6.mul)
    temp_div = session6.new_fn_counter(session6.div)
    assert temp_add(1, 2) == 3, "new_fn_counter does not work as expected"
    assert temp_add(1, 3) == 4, "new_fn_counter does not work as expected"
    assert temp_mul(1, 3) == 3, "new_fn_counter does not work as expected"
    assert temp_div(18, 3) == 6, "new_fn_counter does not work as expected"
    assert temp_div(15, 3) == 5, "new_fn_counter does not work as expected"
    assert temp_div(12, 3) == 4, "new_fn_counter does not work as expected"
    assert session6.d["add"] == 2, "new_fn_counter does not work as expected"
    assert session6.d["mul"] == 1, "new_fn_counter does not work as expected"
    assert session6.d["div"] == 3, "new_fn_counter does not work as expected"


def test_session6_new_fn_counter_unwanted_args():
    with pytest.raises(ValueError, match=r".*Unwanted Arguments given*"):
        session6.new_fn_counter(session6.add, session6.mul)(1, 2)


def test_session6_new_fn_counter_wrong_fn():
    def r():
        return None
    with pytest.raises(ValueError, match=r".*Function not in dictionary*"):
        session6.new_fn_counter(r)()


def test_session6_new_fn_counter_wrong_dict():
    session6.d = {"add": -2, "mul": 0, "div": 0}
    with pytest.raises(Warning, match=r".*Count should not be negative*"):
        session6.new_fn_counter(session6.add)(1,2)
    

# mod_new_fn_counter


def test_session6_mod_new_fn_counter_wrong_input():
    with pytest.raises(TypeError, match=r".*Input Function and Dictionary only*"):
        session6.mod_new_fn_counter('sac', 1+2j)
    with pytest.raises(TypeError, match=r".*Input Function and Dictionary only*"):
        session6.mod_new_fn_counter(1+2j, 'sac')


def test_session6_mod_new_fn_counter_output():
    session6.d1 = {"add": 1, "mul": 3, "div": 4}
    temp1 = session6.mod_new_fn_counter(session6.add, session6.d1)
    temp2 = session6.mod_new_fn_counter(session6.mul, session6.d1)
    temp3 = session6.mod_new_fn_counter(session6.div, session6.d1)
    # print(session6.d1)
    assert temp1(1, 2) == 3, "mod_new_fn_counter does not work as expected"
    assert session6.d1["add"] == 2, "mod_new_fn_counter does not work as expected"
    assert temp2(2, 3) == 6, "mod_new_fn_counter does not work as expected"
    assert session6.d1["mul"] == 4, "mod_new_fn_counter does not work as expected"
    assert temp3(8, 4) == 2, "mod_new_fn_counter does not work as expected"
    assert session6.d1["div"] == 5, "mod_new_fn_counter does not work as expected"


def test_session6_mod_new_fn_counter_unwanted_args():
    with pytest.raises(ValueError, match=r".*Unwanted Arguments given*"):
        session6.mod_new_fn_counter(session6.add, session6.d, 1+2j)(1, 2)


def test_session6_mod_new_fn_counter_wrong_fn():
    def r():
        return None
    with pytest.raises(ValueError, match=r".*Function not in dictionary*"):
        session6.mod_new_fn_counter(r, session6.d1)()


def test_session6_mod_new_fn_counter_wrong_dict():
    session6.d1 = {"add": -2, "mul": 0, "div": 0}
    with pytest.raises(Warning, match=r".*Count should not be negative*"):
        session6.mod_new_fn_counter(session6.add,session6.d1)(1, 2)



