
from pathlib import Path
import requests
import datetime
from base64 import b64encode
import json
from logger import logger
from threader import Threader
import sys
import time

def envia_nist(arquivo_nist):
    nist_filepath = Path(arquivo_nist)

    # Verifica se o Nist ja foi enviado para o SISMIGRA
    logfile_nist = Path(sys.argv[0]).parent / 'nists_lidos_enviados.txt'

    if logfile_nist.exists():
        with open(str(logfile_nist), 'r') as fo:
            lista_nists_enviados = fo.read().splitlines()
    else:
        lista_nists_enviados = []

    if arquivo_nist in lista_nists_enviados:
        logger.info(f'Nist ja cadastrado no SISMIGRA. {arquivo_nist}')
        return None

    if not nist_filepath.exists():
        logger.info(f'Arquivo "{arquivo_nist}" nao encontrado.')
        return None

    try:
        from NIST import NIST
        my_nist = NIST(str(nist_filepath))
    except Exception as e:
        print(f'Erro na leitura do nist {arquivo_nist}. {e}')
        return None

    try:
        nascimento = datetime.datetime.strptime(my_nist.get_field('2.035'), '%Y%m%d').strftime('%Y-%m-%d')
    except Exception as e:
        print(f'Erro na data de nascimento. Ignorando a data de nascimento Nist {arquivo_nist}')
        nascimento = ''

    payload = {
        'nome': my_nist.get_field('2.030'),
        'nascimento': nascimento,
        'nacionalidade': my_nist.get_field('2.038'),
        'mae': my_nist.get_field('2.202'),
        'pai': my_nist.get_field('2.201'),
        'cpf': '',
        'rnm': my_nist.get_field('2.013'),
        'passaporte': '',
        'documento': '',
        'sistema': '+SISMIGRA',
        'comentario': '',
        'bnmp': '',
        'foto_arquivo': b64encode(my_nist.get_field('10.999').encode('utf-8')).decode('utf-8')
    }

    # Remove campos 'null' ou 'none'
    payload = {k: v or '' for k, v in payload.items()}

    http_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post('http://10.195.1.11:5000/pessoas', data=json.dumps(payload), headers=http_headers)

    if 200 <= response.status_code < 300:
        logger.info(f'Dossie cadastrado com sucesso! {response.json()["dossie_id"]} - {my_nist.get_field("2.030")} NIST: {arquivo_nist}')
        return arquivo_nist
    else:
        logger.info(f'Erro {response.status_code} ao cadastrar a pessoa. {json.dumps(response.json().get("mensagem", ""))} Pessoa {my_nist.get_field("2.030")} NIST {arquivo_nist}')
        return None

def log_enviados(nist_enviado):
    logfile_nist = Path(sys.argv[0]).parent / 'nists_lidos_enviados.txt'
    with open(str(logfile_nist), 'a') as append_logfile:
        append_logfile.write(f'{nist_enviado}\n')

def obtem_lista_nists_baixados():
    # Le o diretorio de arquivos baixados e cria uma lista com cada nome de arquivo
    lista_itens_existentes = []
    root_dir = Path(__file__).parent / 'nists_lidos'
    for dir in root_dir.iterdir():
        for file in dir.iterdir():
            lista_itens_existentes.append(str(file))

    return lista_itens_existentes

def obter_lista_nists_enviados():
    arquivos_enviados = Path('__file__').parent / 'nists_lidos_enviados.txt'
    lista_arquivos_enviados = []
    if arquivos_enviados.exists():
        with open(str(arquivos_enviados), 'r') as aef:
            lista_arquivos_enviados = aef.read().splitlines()

    return lista_arquivos_enviados

def obtem_ultimo_dia_baixado():
    logfile_nist = Path(sys.argv[0]).parent / 'nists_lidos_enviados.txt'
    with open(str(logfile_nist), 'r') as of:
        lista_nists_enviados = of.read().splitlines()

    lista_dias_enviados = [Path(x).parent.name for x in sorted(lista_nists_enviados)]

    return lista_dias_enviados[-1]

def obtem_novos_nists_baixados():
    lista_nists_baixados = obtem_lista_nists_baixados()
    ultimo_dia_baixado = obtem_ultimo_dia_baixado()

    lista_novos_nists = [x for x in sorted(lista_nists_baixados) if Path(x).parent.name > ultimo_dia_baixado]

    return lista_novos_nists

if __name__ == '__main__':

    lista_nists = list(set(obtem_lista_nists_baixados()) - set(obter_lista_nists_enviados()))

    threader = Threader(lista_nists, envia_nist, log_enviados, workers=50)

    # Aguarda o threader enccerrar o processamento
    while True:
        time.sleep(1)
        if threader.finished:
            break

    lista_sucesso = [x for x in threader.response_list if x is not None]

    logger.info(f'{len(lista_sucesso)} dossies cadastrados com sucesso!')
