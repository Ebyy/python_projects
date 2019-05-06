#! python3
# pw.py - An insecure password locker program

PASSWORDS = {'email': 'E7beRe0ohgK',
             'blog': 'heh9f7mahbIknuMY92',
             'luggage': 'OKE52erE3hi'}

import sys
if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()
