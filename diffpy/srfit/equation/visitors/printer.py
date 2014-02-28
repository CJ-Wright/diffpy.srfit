#!/usr/bin/env python
########################################################################
#
# diffpy.srfit      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2008 The Trustees of Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
########################################################################
"""Printer visitor for printing the equation represented by a Literal tree.

The Printer visitor creates a one-line representation of the Literal tree,
which is valid as a string equivalent of the equation.

"""
__all__ = ["Printer"]

from diffpy.srfit.equation.visitors.visitor import Visitor

class Printer(Visitor):
    """Printer for printing a Literal tree.

    Attributes:
    output  --  The output generated by the printer.

    """

    def __init__(self):
        """Initialize."""
        self.reset()
        return

    def reset(self):
        """Reset the out put string."""
        self.output = ""
        return

    def onArgument(self, arg):
        """Process an Argument node.

        No assumption is made about the argument type.

        """
        if arg.name is None:
            self.output += str(arg.value)
        else:
            self.output += str(arg.name)
        return self.output

    def onOperator(self, op):
        """Process an Operator node."""
        # We have to deal with infix operators
        if op.name != op.symbol and op.nin == 2:
            self._onInfix(op)
            return

        self.output += str(op.name) + "("

        for idx, literal in enumerate(op.args):
            if idx != 0: self.output += ", "
            literal.identify(self)

        self.output += ")"
        return self.output

    def _onInfix(self, op):
        """Process infix operators."""

        self.output += "("
        op.args[0].identify(self)
        self.output += " %s "%op.symbol
        op.args[1].identify(self)
        self.output += ")"
        return

# End of file
