"""Test for kata_1 binary search."""
import pytest
from quick_katas.kata_1 import userid_list_check
from quick_katas.kata_1 import random_user
from quick_katas.kata_1 import kata_helper

ID_TABLE = [
	[('2z7z7Z2', ['nope123', 'test456', '789isnt', 'ABCh012']), False],
	[('2z7z7Z2', ['1l1l1ll', '2z7z7Z2', 'A4A8BO0', 'GvRBDFL']), True],
	[('z7z7ZZ2', ['wlp4s0x', 'enp0s25', '8675309', 'z7z7ZZ2']), True],
]

@pytest.mark.parametrize("test_args, result", ID_TABLE)
def test_multiple_passes(test_args, result):
	"""Test that main function correctly determines list membership."""
	assert userid_list_check(test_args) == result

def test_alnum():
	"""Test that user IDs are alphanumeric."""
	test_userid = random_user()
	assert test_userid.isalnum()

def test_list_size():
	"""Test that sample list size is correct."""
	helper_args = kata_helper()
	assert len(helper_args[1]) ==  500

def test_userid_len():
	"""I'm definitely looking at my coverage report here."""
	helper_args = kata_helper()
	assert len(helper_args[0]) == 15
