quick-katas
===========

.. image:: https://travis-ci.org/rveeblefetzer/quick-katas.png
   :target: https://travis-ci.org/rveeblefetzer/quick-katas
   :alt: Latest Travis CI build status

Solutions to a couple interesting kata-like problems I heard. One main paramater to the exercise was to write it for Python 2.7.10 with no external imports.   

Usage
-----
kata_1.py
^^^^^^^^^
``userid_list_check(id_inputs)``
Take a tuple of a user ID and a list of user IDs, and return whether the user is in the list. 
It calls sorted() on the user ID list and then runs binary search. In py27 you could pass the tuple into a function,
but this was deprecated in `PEP 3113 <https://www.python.org/dev/peps/pep-3113/>`_, so this straddles compatibility
with indexing.

kata_2.py
^^^^^^^^^
``ip_check(array)``
Take an array of IP addresses and return a list of namedtuples with a type attribute noting if it's a public or private
address. This could've maybe used two lists or a dictionary, but with namedtuple it could be easily rewritten to
include whitelist or blacklist info, or sent to ``._asdict()`` and extended to include a counter for keeping track of
number of connections.

If I were to create an issue for this, it'd be to cover non-addresses, such as octets that go past eight bits.
But instead of going forth with this, there's a really nice solution in the ``_is_private_ip()`` function from Cuckoo Sandbox `here <https://github.com/cuckoosandbox/cuckoo/blob/master/cuckoo/processing/network.py>`_, using the struct
and socket libraries. Struct, which does conversions between Python values and C structs, was new to me, but is
absolutely suited for the problem. And, `the docs for it <https://docs.python.org/2/library/struct.html>`_ has this gem:
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
