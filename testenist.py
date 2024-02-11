from NIST import NIST
import io
from pathlib import Path
import json
from base64 import b64encode, b64decode
from datetime import datetime


arquivo_nist = r'./download\202007231646204053190120240940.nst'

with open(arquivo_nist, 'rb') as file:
    nist_stream = file.read()

my_nist = NIST(nist_stream)
print(my_nist)

# try:
#     nascimento = datetime.strptime(my_nist.get_field('2.035'), '%Y%m%d').strftime('%Y-%m-%d')
# except Exception as e:
#     print(f'Erro na data de nascimento. Ignorando a data de nascimento Nist {arquivo_nist}')
#     nascimento = ''

# pessoa = {
#     'nome': my_nist.get_field('2.030'),
#     'nascimento': nascimento,
#     'nacionalidade': my_nist.get_field('2.038'),
#     'mae': my_nist.get_field('2.202'),
#     'pai': my_nist.get_field('2.201'),
#     'cpf': '',
#     'rnm': my_nist.get_field('2.013'),
#     'passaporte': '',
#     'documento': '',
#     'sistema': '+SISMIGRA',
#     'comentario': '',
#     'bnmp': '',
    
# }


# print(json.dumps(pessoa, indent=4))

foto = my_nist.get_field('10.999')
foto = foto.encode('iso-8859-1')
print(type(foto))
with open('foto.jpg', 'wb') as fp:
    fp.write(foto)

# digital = my_nist.get_field(tag=4, idc=999)
# print(type(digital))
# with open('digital.jpg', 'wb') as fp:
#     fp.write(digital)


