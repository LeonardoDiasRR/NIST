from NIST import NIST

new_nist = NIST()
new_nist.add_Type01()
new_nist.add_Type02()

# Define character encoding and version according to the
# ANSI/NIST-ITL 1-2011 Update 2015 (Edition 3) specification
new_nist.set_field('1.002', 'UTF-8', idc=0)
new_nist.set_field('1.007', '0300', idc=0)

new_nist.set_field('1.008', 'PF/SISMIGRA', idc=0)  # Base de Origem
new_nist.set_field('2.030', 'JÚLIA FIONA ROBERTS', idc=0)  # Nome
new_nist.set_field('2.035', '19671028', idc=0)  # Data de nascimento
new_nist.set_field('2.037', 'Smyrna/GA', idc=0)  # Cidade de nascimento
new_nist.set_field('2.038', '2038', idc=0)  # País de nascimento
new_nist.set_field('2.039', '2', idc=0)  # Sexo 1|M-Masculino, 2|F-Feminino, ?|O-Outros
new_nist.set_field('2.201', 'PAI DA JÚLIA', idc=0)  # Pai
new_nist.set_field('2.202', 'MÃE DA ROBERTS', idc=0)  # Mae
# new_nist.set_field('2.211', '130692-SSP-RR')  # Identidade
# new_nist.set_field('2.212', '', idc=0),  # CPF
# new_nist.set_field('2.213', '', idc=0)  # Titulo de eleitor
# new_nist.set_field('2.214', '', idc=0)  # CNH
# new_nist.set_field('2.224', 'JULIA ROBERTS')  # Nome social

# Faces
faces = [
    'amostras/fotos/JuliaRoberts.jfif'
]
new_nist.add_ntype(10)
for index, face in enumerate(faces, start=1):
    with open(face, 'rb') as f:
        face = f.read()
        new_nist.set_field('10.999', face, idc=index)

# Digitais
# new_nist.add_ntype(4)
# new_nist.set_field('4.001', 4, idc=1)  # Record Type (TYP) [Mandatory]
# new_nist.set_field('4.002', 0, idc=1)  # Image Designation Character (IDC) [Mandatory]
# new_nist.set_field('4.003', 1, idc=1)  # Impression Type (IMP) [Mandatory]
# new_nist.set_field('4.004', 1, idc=1)  # Image Horizontal Line Length (HLL) [Mandatory]
# new_nist.set_field('4.005', 1, idc=1)  # Image Vertical Line Length (VLL) [Mandatory]
# new_nist.set_field('4.006', 800, idc=1)  # Fingerprint Image Scanning Resolution (FIR) [Mandatory]
# new_nist.set_field('4.007', 750, idc=1)  # Finger Position (FGP) [Mandatory]
# new_nist.set_field('4.008', 1, idc=1)  # Print Position Coordinates (PPC) [Optional]
# new_nist.set_field('4.014', 'WSQ', idc=1)  # Image Compression Algorithm (ICA) [Mandatory]
# 
# # Adiciona o dedo plegar direito (idc=1)
# # with open(f'amostras\digitais\digital_1.wsq', 'rb') as f:
# #     digital = f.read()
#     new_nist.set_field('4.999', digital, idc=1)

# Salva o nist no disco
new_nist.write('novo_nist_2015.nst')

print(new_nist)
