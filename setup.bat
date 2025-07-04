@echo off
SETLOCAL

:: Caminho do ambiente virtual
SET VENV_DIR=venv

echo [1/5] Criando ambiente virtual em %VENV_DIR%...
python3.12 -m venv %VENV_DIR%
IF ERRORLEVEL 1 (
    echo Erro ao criar o ambiente virtual.
    EXIT /B 1
)

echo [2/5] Ativando ambiente virtual...
CALL %VENV_DIR%\Scripts\activate.bat
IF ERRORLEVEL 1 (
    echo Erro ao ativar o ambiente virtual.
    EXIT /B 1
)

echo [3/5] Atualizando pip...
python -m pip install --upgrade pip
IF ERRORLEVEL 1 (
    echo Erro ao atualizar pip.
    EXIT /B 1
)

echo [4/6] Instalando dependências do requirements.txt...
IF EXIST requirements.txt (
    pip install -r requirements.txt
    IF ERRORLEVEL 1 (
        echo Erro ao instalar dependências.
        EXIT /B 1
    )
) ELSE (
    echo Arquivo requirements.txt não encontrado. Nenhuma dependência instalada.
)

:: Diretório que contém as bibliotecas obrigatórias
SET LIBS_DIR=libs

echo [5/6] Instalando dependências das bibliotecas...
FOR %%L IN (NIST MDmisc PMlib WSQ) DO (
    IF EXIST "%LIBS_DIR%\%%L\requirements.txt" (
        echo Instalando dependencias de %LIBS_DIR%\%%L\requirements.txt...
        pip install -r "%LIBS_DIR%\%%L\requirements.txt"
        IF ERRORLEVEL 1 (
            echo Erro ao instalar dependencias de %LIBS_DIR%\%%L.
            EXIT /B 1
        )
    )
)

:: Cria arquivo .pth apontando para as bibliotecas
FOR /F "delims=" %%p IN ('python -c "import site; print(site.getsitepackages()[0])"') DO SET SITE_PACKAGES=%%p
SET PTH_FILE=%SITE_PACKAGES%\mdedonno.pth
echo Criando %PTH_FILE%...
( 
    echo %CD%\libs\NIST
    echo %CD%\libs\WSQ
    echo %CD%\libs\PMlib
    echo %CD%\libs\MDmisc
) > "%PTH_FILE%"
echo %PTH_FILE% criado.

echo [6/6] Setup concluído com sucesso.
ENDLOCAL
