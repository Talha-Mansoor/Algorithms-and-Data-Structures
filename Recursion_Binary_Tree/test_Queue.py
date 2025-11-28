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


import SimpleQueue as Queue


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
    aqueue = Queue.SimpleQueue()
    assert isinstance(aqueue, Queue.SimpleQueue), 'Test fault: __init__ failed'


def test_1():
    test_objective = 'is_empty()'
    reason = 'empty queue'
    aqueue = Queue.SimpleQueue()
    result = aqueue.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_2():
    test_objective = 'size()'
    reason = 'empty queue'
    aqueue = Queue.SimpleQueue()
    result = aqueue.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3():
    test_objective = 'is_empty()'
    reason = 'queue with one value'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_4():
    test_objective = 'size()'
    reason = 'queue with one value'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    result = aqueue.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_5():
    test_objective = 'peek()'
    reason = 'enqueued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    result = aqueue.peek()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_6():
    test_objective = 'size()'
    reason = 'enqueued 1 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    ignore = aqueue.peek()
    result = aqueue.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_7():
    test_objective = 'isempty()'
    reason = 'enqueued 1 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    ignore = aqueue.peek()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_8():
    test_objective = 'dequeue()'
    reason = 'enqueued 1 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    result = aqueue.dequeue()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_9():
    test_objective = 'is_empty()'
    reason = 'enqueued 1 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    temp = aqueue.dequeue()
    result = aqueue.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_10():
    test_objective = 'size()'
    reason = 'enqueued 1 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('value')
    temp = aqueue.dequeue()
    result = aqueue.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_11():
    test_objective = 'size()'
    reason = 'enqueued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    result = aqueue.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_12():
    test_objective = 'is_empty()'
    reason = 'enqueued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_13():
    test_objective = 'peek()'
    reason = 'enqueued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    result = aqueue.peek()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14():
    test_objective = 'size()'
    reason = 'enqueued 2 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    ignore = aqueue.peek()
    result = aqueue.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_15():
    test_objective = 'is_empty()'
    reason = 'enqueued 2 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    ignore = aqueue.peek()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_16():
    test_objective = 'dequeue()'
    reason = 'enqueued 2 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    result = aqueue.dequeue()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_17():
    test_objective = 'size()'
    reason = 'enqueued 2 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    temp = aqueue.dequeue()
    result = aqueue.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_18():
    test_objective = 'is_empty()'
    reason = 'enqueued 2 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    temp = aqueue.dequeue()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_19():
    test_objective = 'peek()'
    reason = 'enqueued 2 then dequeued 1'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    ignore = aqueue.dequeue()
    result = aqueue.peek()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_20():
    test_objective = 'size()'
    reason = 'enqueued 2 then dequeued 1 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    ignore = aqueue.dequeue()
    ignore = aqueue.peek()
    result = aqueue.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_21():
    test_objective = 'is_empty()'
    reason = 'enqueued 2 then dequeued 1 then peeked'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    ignore = aqueue.dequeue()
    ignore = aqueue.peek()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_22():
    test_objective = 'is_empty()'
    reason = 'enqueued 2 then dequeued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    temp = aqueue.dequeue()
    temp = aqueue.dequeue()
    result = aqueue.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_23():
    test_objective = 'size()'
    reason = 'enqueued 2 then dequeued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    temp = aqueue.dequeue()
    temp = aqueue.dequeue()
    result = aqueue.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_24():
    test_objective = 'dequeue()'
    reason = 'enqueued 2 then dequeued 2'
    aqueue = Queue.SimpleQueue()
    aqueue.enqueue('first')
    aqueue.enqueue('second')
    temp = aqueue.dequeue()
    result = aqueue.dequeue()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_25():
    test_objective = 'size()'
    reason = 'enqueued 10'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    result = aqueue.size()
    expected = 10
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_26():
    test_objective = 'is_empty()'
    reason = 'enqueued 10'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_27():
    test_objective = 'peek()'
    reason = 'enqueued 10'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    result = aqueue.peek()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_28():
    test_objective = 'dequeue()'
    reason = 'enqueued 10'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    result = aqueue.dequeue()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_29():
    test_objective = 'is_empty()'
    reason = 'enqueued 10 dequeued 1'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    ignore = aqueue.dequeue()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_30():
    test_objective = 'size()'
    reason = 'enqueued 10 dequeued 1'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    ignore = aqueue.dequeue()
    result = aqueue.size()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_31():
    test_objective = 'peek()'
    reason = 'enqueued 10 dequeued 1'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    ignore = aqueue.dequeue()
    result = aqueue.peek()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_32():
    test_objective = 'is_empty()'
    reason = 'enqueued 10 dequeued 7'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    for i in range(7):
        ignore = aqueue.dequeue()
    result = aqueue.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_33():
    test_objective = 'size()'
    reason = 'enqueued 10 dequeued 7'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    for i in range(7):
        ignore = aqueue.dequeue()
    result = aqueue.size()
    expected = 3
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_34():
    test_objective = 'peek()'
    reason = 'enqueued 10 dequeued 7'
    stuff = list(range(10))
    aqueue = Queue.SimpleQueue()
    for st in stuff:
        aqueue.enqueue(st)
    for i in range(7):
        ignore = aqueue.dequeue()
    result = aqueue.peek()
    expected = 7
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
