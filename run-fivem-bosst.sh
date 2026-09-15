#!/bin/bash

# FiveM PC Booster - Linux/macOS Runner

echo ""
echo "╔════════════════════════════════════════╗"
echo "║   FiveM PC Booster - Otimizador v1.0   ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python 3 nao encontrado!"
    echo "Instale com: sudo apt install python3 python3-pip"
    exit 1
fi

echo "Verificando dependencias..."
pip install -r requirements.txt

echo "Executando FiveM PC Booster..."
echo ""
python3 main.py
