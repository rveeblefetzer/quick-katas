quick-katas
===========

.. image:: https://travis-ci.org/rveeblefetzer/quick-katas.png
   :target: https://travis-ci.org/rveeblefetzer/quick-katas
   :alt: Latest Travis CI build status

Solutions to a couple kata-like problems I heard. 

Usage
-----
kata_1.py:
userid_list_check(id_inputs)
Takes a tuple of a user ID and a list of user IDs, and returns whether the user is in the list. 
It calls sorted() on the user ID list and then runs binary search.


kata_2.py
ip_check(array)
Takes an array of IP addresses and returns a list of namedtuples with a type attribute noting 
if it's a public or private address. Could've used two lists or a dictionary, but this way it could be
rewritten to include whitelist or blacklist info, or sent to ._asdict() to include a counter for number
of connections.

Requirements
^^^^^^^^^^^^
Just the standard library -- string, random, collections. Pytest, tox and pytest-cov for tests.

Compatibility
-------------
Tested for Python 2.7.10, 3.5.4, 3.6.4

Licence
-------
MIT

Authors
-------
`quick-katas` was written by `Rick Valenzuela <rv@rickv.com>`_.
