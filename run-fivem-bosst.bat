@echo off
REM ============================================
REM FiveM PC Booster - Windows Runner
REM ============================================

color 0A
echo.
echo  ╔════════════════════════════════════════╗
echo  ║   FiveM PC Booster - Otimizador v1.0   ║
echo  ╚════════════════════════════════════════╝
echo.
echo  Iniciando aplicacao...
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    color 4C
    echo  [ERRO] Python nao encontrado!
    echo  Baixe em: https://www.python.org
    pause
    exit /b 1
)

REM Instalar dependencias
echo  Verificando dependencias...
pip install -r requirements.txt >nul 2>&1

echo  Executando...
echo.
python main.py

pause
