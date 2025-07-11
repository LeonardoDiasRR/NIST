Python NIST library
###################

Welcome to the documentation of the python NIST library. The aim of the python library is to open, modify and write Biometric Information files based on the standard proposed by the NIST (for short: NIST format) [NIST2013]_.

This python library contains a main module to read and write NIST files (named 'NIST.traditional'), and a second module to work with fingerprint related NIST files (named 'NIST.fingerprint'). Some complementary modules are provided for some particular cases.

The library now includes defaults for record Types 16 through 22 and 98 as defined in the ANSI/NIST-ITL 1-2011 Update: 2015 standard. New helper methods ``add_Type16`` to ``add_Type22`` and ``add_Type98`` simplify creating these records.

The developpement and maintainance have been made by Marco De Donno, School of Criminal Justice, Faculty of Law, Criminal Justice and Public Administration, University of Lausanne, Switzerland. This library is not related to the National Institute of Standards and Technology.

.. [NIST2013] Data Format for the Interchange of Fingerprint, Facial & Other Biometric Information, NIST Special Publication 500-290 Rev1 (2013), https://www.nist.gov/itl/iad/image-group/ansinist-itl-standard-references

Encoding
========

Earlier versions of this package decoded all text sections as ``UTF-8``.
Some real-world NIST files contain byte values outside of that encoding,
resulting in ``UnicodeDecodeError`` during parsing.  The library now uses
``latin-1`` when reading, writing or hashing textual fields to preserve
the original byte content.

Binary payloads such as JPEG or WSQ images can now be passed to
``set_field`` directly as ``bytes``.  The library converts them to its
internal ``latin-1`` representation automatically.  Accessing these
fields via ``get_field`` returns the original ``bytes`` object so callers
no longer need to manually encode or decode the data.


