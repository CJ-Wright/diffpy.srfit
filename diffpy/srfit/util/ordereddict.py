########################################################################
#
# diffpy.srfit      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2008 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

"""Import OrderedDictionary from python > 2.7/3.1 for earlier python versions.

"""

__all__ = ["OrderedDict"]

try:
    from collections import OrderedDict
except ImportError:
    from _ordereddict import OrderedDict


# End of file