# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.

# CMPT 145: Object Oriented Programming
# 202001 Assignment 10 Question 2


import Stack as Stack


def str_form(obj, result, exp, reason):
    """
    Purpose:
        Abbreviate test case assertions.
    Preconditions:
        :param obj:  a string
        :param result: a value
        :param reason: a string
    :return: a string
    """
    return ' '.join(['Test fault:',obj,
                     'returned',str(result),
                     '(expected:', str(exp)+')',
                     'on:',reason])


def test_0():
    astack = Stack.Stack()
    assert isinstance(astack, Stack.Stack), 'Test fault: __init__ failed'


def test_1():
    test_objective = 'is_empty()'
    reason = 'empty stack'
    astack = Stack.Stack()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_2():
    test_objective = 'size()'
    reason = 'empty stack'
    astack = Stack.Stack()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3():
    test_objective = 'is_empty()'
    reason = 'stack with one value'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_4():
    test_objective = 'size()'
    reason = 'stack with one value'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_5():
    test_objective = 'peek()'
    reason = 'pushed 1'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.peek()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_6():
    test_objective = 'size()'
    reason = 'pushed 1 then peeked'
    astack = Stack.Stack()
    astack.push('value')
    ignore = astack.peek()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_7():
    test_objective = 'isempty()'
    reason = 'pushed 1 then peeked'
    astack = Stack.Stack()
    astack.push('value')
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_8():
    test_objective = 'pop()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.pop()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_9():
    test_objective = 'is_empty()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    temp = astack.pop()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_10():
    test_objective = 'size()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    temp = astack.pop()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_11():
    test_objective = 'size()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_12():
    test_objective = 'is_empty()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_13():
    test_objective = 'peek()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.peek()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14():
    test_objective = 'size()'
    reason = 'pushed 2 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.peek()
    result = astack.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_15():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_16():
    test_objective = 'pop()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.pop()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_17():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_18():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_19():
    test_objective = 'peek()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    result = astack.peek()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_20():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 1 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    ignore = astack.peek()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_21():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 1 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_22():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    temp = astack.pop()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_23():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    temp = astack.pop()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_24():
    test_objective = 'pop()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.pop()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_25():
    test_objective = 'size()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.size()
    expected = 10
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_26():
    test_objective = 'is_empty()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_27():
    test_objective = 'peek()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.peek()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_28():
    test_objective = 'pop()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.pop()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_29():
    test_objective = 'is_empty()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_30():
    test_objective = 'size()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.size()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_31():
    test_objective = 'peek()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.peek()
    expected = 8
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_32():
    test_objective = 'is_empty()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_33():
    test_objective = 'size()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.size()
    expected = 3
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_34():
    test_objective = 'peek()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.peek()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

all_of_em = [
        test_0,
        test_1,
        test_2,
        test_3,
        test_4,
        test_5,
        test_6,
        test_7,
        test_8,
        test_9,
        test_10,
        test_11,
        test_12,
        test_13,
        test_14,
        test_15,
        test_16,
        test_17,
        test_18,
        test_19,
        test_20,
        test_21,
        test_22,
        test_23,
        test_24,
        test_25,
        test_26,
        test_27,
        test_28,
        test_29,
        test_30,
        test_31,
        test_32,
        test_33,
        test_34,
    ]

count = 0
failed = 0
for t in reversed(all_of_em):
    count += 1
    try: 
        t()
    except Exception as e:
        print("Test failure in function:", t.__name__)
        print(e)
        print()
        failed += 1


print('Passed', count - failed, 'out of total', count, 'tests')
if failed > 2:
    print('***Note***\nThe tests were executed in reverse order, so you can\nmore easily see the first test failures.')
