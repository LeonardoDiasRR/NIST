#!/bin/bash

# Interrompe o script se qualquer comando falhar
set -e

# Caminho para o ambiente virtual
VENV_DIR="./venv"

echo "➡️ Criando ambiente virtual em $VENV_DIR..."
python3 -m venv "$VENV_DIR"

echo "✅ Ambiente virtual criado."

# Ativa o ambiente virtual
echo "➡️ Ativando ambiente virtual..."
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo "✅ Ambiente virtual ativado."

# Atualiza o pip
echo "➡️ Atualizando pip..."
pip install --upgrade pip

echo "✅ pip atualizado."


# Instala dependências do projeto principal
if [ -f "requirements.txt" ]; then
    echo "➡️ Instalando dependências de requirements.txt..."
    pip install -r requirements.txt
    echo "✅ Dependências instaladas."
else
    echo "⚠️ Arquivo requirements.txt não encontrado. Nenhuma dependência instalada."
fi

# Diretório contendo as bibliotecas obrigatórias
LIBS_DIR="./libs"

# Instala dependências das bibliotecas auxiliares
for lib in NIST MDmisc PMlib WSQ; do
    LIB_PATH="$LIBS_DIR/$lib"
    if [ -f "$LIB_PATH/requirements.txt" ]; then
        echo "➡️ Instalando dependências de $LIB_PATH/requirements.txt..."
        pip install -r "$LIB_PATH/requirements.txt"
    fi

done

# Instala bibliotecas da pasta libs no ambiente virtual
echo "➡️ Instalando bibliotecas auxiliares no ambiente virtual..."
python install_nist.py "$VENV_DIR" "$LIBS_DIR/"
echo "✅ Bibliotecas auxiliares instaladas."

echo "✅ Setup concluído com sucesso."
