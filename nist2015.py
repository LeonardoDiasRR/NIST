"""NIST 2015 Edition Interface
=================================

This module provides a high level interface to create, read, update and
write ANSI/NIST biometric files compliant with the specification
*ANSI/NIST-ITL 1-2011 Update 2015 (SP 500-290 Edition 3)*.

It wraps the traditional implementation bundled under ``libs/NIST`` and
exposes convenience helpers for manipulating field values and record
structures.
"""

from NIST import NIST as _BaseNIST


class NIST(_BaseNIST):
    """Wrapper around :class:`NIST.traditional.NIST` for the 2015 edition."""

    def __init__(self, init=None):
        super().__init__(init)

    # ------------------------------------------------------------------
    # File operations
    # ------------------------------------------------------------------
    def read(self, filepath):
        """Load data from ``filepath`` into the object."""
        super().read(filepath)

    def write(self, filepath):
        """Write the current contents to ``filepath``."""
        super().write(filepath)

    # ------------------------------------------------------------------
    # Record management helpers
    # ------------------------------------------------------------------
    def create_type(self, ntype, idc=0):
        """Create a new record of ``ntype`` with the given ``idc``."""
        if ntype == 1:
            self.add_Type01()
        elif ntype == 2:
            self.add_Type02(idc)
        else:
            self.add_default(ntype, idc)

    def delete_type(self, ntype):
        """Remove an entire record ``ntype``."""
        super().delete_ntype(ntype)

    def delete_idc(self, ntype, idc):
        """Delete a specific ``idc`` from ``ntype``."""
        super().delete_idc(ntype, idc)

    # ------------------------------------------------------------------
    # Field level helpers
    # ------------------------------------------------------------------
    def create_field(self, tag, value, idc=0):
        """Create or set a field."""
        self.set_field(tag, value, idc)

    def read_field(self, tag, idc=-1):
        """Return the value of ``tag``."""
        return self.get_field(tag, idc)

    def update_field(self, tag, value, idc=-1):
        """Update ``tag`` with ``value``."""
        self.set_field(tag, value, idc)

    def delete_field(self, tag, idc=-1):
        """Delete ``tag`` from the record."""
        self.delete_tag(tag, idc)

