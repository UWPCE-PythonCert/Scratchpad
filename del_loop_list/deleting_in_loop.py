#!/usr/bin/env python

"""
What happens when you delete from a list while looping through it?
"""

for item in a_list:
    if something(item):
        a_list.remove(item)










a_list = list(range(10))
print("the original", a_list)
# loop to remove almost everything...
for item in a_list[:]:
    if item:  # is it an nonzero number?
        a_list.remove(item)
print("after removing some", a_list)

# is that what you expected?

# what about adding stuff?
a_list = list(range(10))
for item in a_list:
    if item % 2:  # duplicate odd numbers
        a_list.append(item)

print("after adding odd numbers", new_list)


# what about adding stuff?
a_list = list(range(10))
new_list = []
for item in a_list:
    new_list.append(item)
    if item % 2:  # duplicate odd numbers
        new_list.append(item)

print("after adding odd numbers", new_list)
