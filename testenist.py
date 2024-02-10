from NIST import NIST
import io
from pathlib import Path


arquivo = Path(__file__) / r'/download/202007231646204053190120240940.nst'

with open(arquivo, 'rb') as file:
    nist_bin = file

nist = NIST(arquivo)

# print(type(nist_bin))
# if isinstance(nist_bin, io.BufferedReader):
#     print('BufferedReader')
# else:
#     print('formato desconhecido')

# print('FS', chr( 28 ))
# print('GS', chr( 29 ))
# print('RS', chr( 30 ))
# print('US', chr( 31 ))
# CO = ':'
# DO = '.'