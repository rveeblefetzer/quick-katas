"""Tests for kata_2 IP checker."""

import pytest
from quick_katas.kata_2 import ip_check

def test_microsoft_public():
    """Test that Microsoft IP address is classified as public."""
    test_list = ip_check(['127.0.0.1', '192.168.0.1', '207.46.130.0'])
    assert test_list[2].type == 'public'

def test_localhost_private():
    """Test that localhost address is classified as private."""
    test_list = ip_check(['127.0.0.1', '192.168.0.1', '207.46.130.0'])
    assert test_list[0].type == 'private'
