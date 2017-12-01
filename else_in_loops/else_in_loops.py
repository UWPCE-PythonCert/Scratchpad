#!/usr/bin/env python

"""
script to help demonstrate using else in for and while loops
"""

a_list = ["this", "anything", "that", "the other", "more", "or"]


def do_something(*args):
    """ just to have an example function to run"""
    print("I did something")


def do_something_else(*args):
    """ just to have an example function to run"""
    print("I did something else")

###


for item in a_list:
    print(item)

###

for i in range(10):
    print(i)

###

for i, item in enumerate(a_list):
    print(i, item)

###

while i < 10:
    print(i)
    i += 1

###

for item in a_list:
    if item.startswith('t'):
        continue
    print(item)

###

for item in a_list:
    if "the" in item:
        break
    print(item)

###

for item in a_list:
    if 'm' in item:
        do_something()
        break
    print(item)

###

for item in a_list:
    if 'm' in item:
        do_something()
        break
    print(item)
do_something_else()

###

break_was_called = False
for item in a_list:
    if 'm' in item:
        do_something()
        break_was_called = True
        break
    print(item)
if not break_was_called:
    do_something_else()


break_was_called = False
for item in a_list:
    if 'z' in item:
        do_something()
        break_was_called = True
        break
    print(item)
if not break_was_called:
    do_something_else()

###

for item in a_list:
    if 'z' in item:
        do_something()
        break
    print(item)
else:
    do_something_else()

###

for item in a_list:
    if 'm' in item:
        do_something()
        break
    print(item)
else:
    do_something_else()

###

break_was_called = False
for item in a_list:
    if 'z' in item:
        do_something()
        break_was_called = True
        break
    print(item)
if break_was_called:
    pass
else:
    do_something_else()

###

for item in a_list:
    if 'z' in item:
        do_something()
        break
    print(item)
else:
    do_something_else()


