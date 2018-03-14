#!/usr/bin python

"""Functions for a kata-type problem I heard recently.

Given a user ID of letters and numbers, return whether that user is in a list
of users. It calls sorted on the user ID list and then runs binary search.

userid_needle_haystack(userid, id_list) returns True or False whether a userid
is in array; both elements are given in a tuple.

random_user() is a helper function for illustration purposes that creates user
IDs of random strings.

kata_helper() is a helper function for illustration purposes that creates a
list of 500 user IDs and selects one at random.
"""

import random
import string

def userid_list_check(id_inputs):
    """Determine if a user ID is in a list of user IDs."""
    userid = id_inputs[0]
    search_list = sorted(id_inputs[1])
    low = 0
    high = len(search_list) - 1
    counter = 0
    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]
        if guess == userid:
            return True
        if guess > userid:
            high = mid - 1
        else:
            low = mid + 1
        counter += 1
    return False

def random_user():
    """Return a random string."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for x in range(15))

def kata_helper():
    """Return a target user ID and an array."""
    user_list = list(random_user() for x in range(500))
    in_or_out = random.choice([0,1])
    if in_or_out == 0:
        target_user = random_user()
    else:
        target_user = random.choice(user_list)
    return (target_user, user_list)

if __name__ == '__main__':
    if userid_list_check(kata_helper()) == False:
        print('False')
    else:
        print('True')

