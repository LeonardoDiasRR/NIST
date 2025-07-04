#!/bin/bash

# Interrompe o script se qualquer comando falhar
set -e

# Caminho para o ambiente virtual
VENV_DIR="./venv"

echo "➡️ Criando ambiente virtual em $VENV_DIR..."
python3.12 -m venv "$VENV_DIR"

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

# Cria arquivo .pth para tornar as bibliotecas visíveis ao Python
SITE_PACKAGES=$(python - <<'EOF'
import site
print(site.getsitepackages()[0])
EOF
)
PTH_FILE="$SITE_PACKAGES/mdedonno.pth"

echo "➡️ Criando $PTH_FILE..."
printf "%s\n" \
    "$(pwd)/libs/NIST" \
    "$(pwd)/libs/WSQ" \
    "$(pwd)/libs/PMlib" \
    "$(pwd)/libs/MDmisc" \
    > "$PTH_FILE"
echo "✅ $PTH_FILE criado."

echo "✅ Setup concluído com sucesso."
