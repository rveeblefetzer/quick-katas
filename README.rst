quick-katas
===========

.. image:: https://travis-ci.org/rveeblefetzer/quick-katas.png
   :target: https://travis-ci.org/rveeblefetzer/quick-katas
   :alt: Latest Travis CI build status

Solutions to a couple kata-like problems I heard. One main paramater to the exercise was to write it for Python 2.7.10 and only using the standard library.   

Usage
-----
kata_1.py
^^^^^^^^^
userid_list_check(id_inputs)
Take a tuple of a user ID and a list of user IDs, and return whether the user is in the list. 
It calls sorted() on the user ID list and then runs binary search.

kata_2.py
^^^^^^^^^
ip_check(array)
Take an array of IP addresses and return a list of namedtuples with a type attribute noting 
if it's a public or private address. Could've used two lists or a dictionary, but this way it could be
rewritten to include whitelist or blacklist info, or sent to ._asdict() to include a counter for number
of connections.

Otherwise, though, the solution to this problem is so well done in the `_is_private_ip()` function by William Metcalf
`here <https://github.com/wmetcalf/cuckoo-master/blob/master/modules/processing/network.py>`, using the struct and sockets libraries. Struct, which does coversions between Python values and C structs, was new to me, but is absolutely suited for the problem. Also, `the docs <https://docs.python.org/2/library/struct.html>` has this gem:
	The form '!' is available for those poor souls who claim they can’t remember whether network byte order is big-endian or little-endian.

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
