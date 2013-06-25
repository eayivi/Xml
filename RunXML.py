#
# Enam Ayivi
# aea787
# Paul Carroll
# pvc95
#

"""
To run the program
    % python RunXML.py < RunXML.in > RunXML.out
    % chmod ugo+x RunXML.py
    % RunXML.py < RunXML.in > RunXML.out

To document the program
    % pydoc -w XML
"""

# -------
# imports
# -------

import sys

from XML import xml_solve

# ----
# main
# ----

xml_solve(sys.stdin, sys.stdout)
