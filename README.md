# NIST

Este projeto fornece uma versão **adaptada para Python&nbsp;3** do repositório
[mdedonno1337/NIST](https://github.com/mdedonno1337/NIST), originalmente
escrito em Python&nbsp;2.7. O objetivo principal é possibilitar a criação, a
leitura e a modificação de arquivos no formato ANSI/NIST de maneira simples,
mantendo compatibilidade com os dados gerados pela implementação original.

O diretório `libs/` contém versões incorporadas das seguintes bibliotecas:

- **NIST** – núcleo para decodificar, manipular e gerar arquivos NIST.
- **MDmisc** – funções auxiliares diversas (manipulação binária, logs, etc.).
- **PMlib** – ferramentas de processamento de imagens e conversão de formato.
- **WSQ** – utilitários para compressão e descompressão em formato WSQ.

## Ambiente

Use `setup.sh` (Linux) ou `setup.bat` (Windows) para criar o ambiente virtual `venv` e instalar as dependências. Após a instalação ative o ambiente com:

```bash
source venv/bin/activate
```

ou, no Windows:

```cmd
venv\Scripts\activate.bat
```

## Exemplos

- `create_nist_example.py` cria um arquivo NIST de exemplo com fotos e digitais.
- `load_nist_example.py` carrega um arquivo existente e gera uma cópia.

## Como criar ou carregar um arquivo NIST

O módulo principal expõe a classe `NIST`, responsável por manipular as
estruturas do padrão ANSI/NIST. Para criar um novo arquivo:

```python
from NIST import NIST

nist = NIST()
nist.add_Type01()  # registro de cabeçalho
nist.set_field('1.003', 'AGÊNCIA', idc=0)
nist.write('meu_arquivo.nst')
```

Para ler um arquivo existente e alterar algum campo:

```python
from NIST import NIST

nist = NIST('entrada.nst')
data_nascimento = nist.get_field('2.035', idc=0)
nist.set_field('2.035', '19800101', idc=0)
nist.write('saida.nst')
```

## Documentação

Arquivos PDF de referência estão em `docs/`. A biblioteca `libs/NIST` contém documentação detalhada em `libs/NIST/doc/`.

Este projeto não possui qualquer vínculo com o National Institute of Standards and Technology (NIST) original.
