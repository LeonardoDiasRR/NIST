import os
from NIST import NIST

if __name__ == '__main__':
    sample_path = os.path.join('amostras', 'nists', 'sinpa', '120080001610875010220091414.nst')
    mynist = NIST(sample_path)
    print(mynist)
