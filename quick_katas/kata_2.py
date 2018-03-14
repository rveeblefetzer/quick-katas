"""Given a list of IP addresses, determine whether each is public or private.

Function splits each IP addess and checks if first two octets fall under
specific ranges for private, loopback or diagnostic addresses; the address is
then put into a namedtuple class with a corresponding attribute for IP type. Returns list of namedtuples.
"""

from collections import namedtuple
import sys

def ip_check(array):
    """Return list of categorized IP addresses."""
    checked_ips = list()
    Ip_addr = namedtuple('Ip_addr', 'address type')
    for ip in array:
        ip_split = ip.split('.')
        if int(ip_split[0]) == 10:
            ip = Ip_addr(ip, 'private')
        elif int(ip_split[0]) == 127:
            ip = Ip_addr(ip, 'private')
        elif int(ip_split[0]) == 172:
            if int(ip_split[1]) in range(16,32):
                ip = Ip_addr(ip, 'private')
        elif int(ip_split[0]) == 192 and int(ip_split[1]) == 168:
            ip = Ip_addr(ip, 'private')
        elif int(ip_split[0]) > 223:
            ip = Ip_addr(ip, 'private')
        else:
            ip = Ip_addr(ip, 'public')
        checked_ips.append(ip)
    return checked_ips

if __name__ == '__main__':
    array = sysargv[1]
    ip_check(array)
    sys
