import os
import random
import string
import sys

sys.path[0:0] = [
    os.path.join('libs', 'NIST'),
    os.path.join('libs', 'MDmisc'),
    os.path.join('libs', 'PMlib'),
    os.path.join('libs', 'WSQ'),
]

from NIST import NISTf


def random_text(length=8, digits=False):
    chars = string.digits if digits else string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def fill_random_fields(nist):
    for ntype in nist.get_ntype():
        if ntype == 1:
            continue
        for idc in nist.get_idc(ntype):
            for tagid in list(nist.data[ntype][idc].keys()):
                if tagid in (1, 4):
                    continue
                value = nist.get_field((ntype, tagid), idc)
                if value is None:
                    continue
                if isinstance(value, bytes):
                    nist.set_field((ntype, tagid), os.urandom(max(1, len(value))), idc)
                else:
                    digits = value.isdigit() or value == ''
                    nist.set_field((ntype, tagid), random_text(max(1, len(str(value))), digits), idc)


if __name__ == "__main__":
    
    nist = NISTf()
    nist.add_Type01()
    nist.add_Type02()

    nist.add_Type04()
    nist.set_field("4.999", os.urandom(10), 1)

    # from NIST.fingerprint.functions import AnnotationList
    # nist.add_Type09()
    # m = AnnotationList()
    # m.from_list([[1, 1.0, 1.0, 0, 0, 'A']], format="ixytqd", type="Minutia")
    # nist.set_minutiae(m, 0)
    nist.add_Type13()
    nist.set_field("13.999", os.urandom(10), 0)
    nist.add_Type14()
    nist.set_field("14.999", os.urandom(10), 1)
    nist.add_Type15()
    nist.set_field("15.999", os.urandom(10), 1)
    nist.add_Type16()
    nist.add_Type17()
    nist.add_Type18()
    nist.add_Type19()
    nist.add_Type20()
    nist.add_Type21()
    nist.add_Type22()
    nist.add_Type98()

    nist.add_idc(10, 0)
    nist.set_field("10.002", 0, 0)
    nist.set_field("10.999", os.urandom(10), 0)

    nist.add_idc(99, 0)
    nist.set_field("99.002", 0, 0)
    nist.set_field("99.999", os.urandom(10), 0)

    fill_random_fields(nist)

    print("Created NIST with types:", nist.get_ntype())

    print(nist)

    nist.write('created_all_types_nist_example.nst')    
    print('Nist salvo no disco.')
    

    
    
