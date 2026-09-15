#!/usr/bin/env python3
"""
Script de Configuração - FiveM PC Booster
Instala dependências automaticamente
"""

import subprocess
import sys
import os

def print_header():
    print("\n" + "="*50)
    print("  FiveM PC Booster - Setup Automático")
    print("="*50 + "\n")

def check_python():
    print("[1/4] Verificando Python...")
    version = sys.version_info
    print(f"  ✓ Python {version.major}.{version.minor}.{version.micro} encontrado\n")
    
    if version.major < 3 or version.minor < 8:
        print("  ⚠️  Python 3.8+ recomendado!")
        return False
    return True

def check_pip():
    print("[2/4] Verificando pip...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ {result.stdout.strip()}\n")
            return True
    except:
        pass
    
    print("  ✗ pip não encontrado\n")
    return False

def install_dependencies():
    print("[3/4] Instalando dependências...")
    
    requirements = [
        'psutil==5.9.5',
        'PyQt6==6.6.1',
        'requests==2.31.0',
        'colorama==0.4.6',
        'python-dotenv==1.0.0',
    ]
    
    try:
        for package in requirements:
            print(f"  Instalando {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package],
                         capture_output=True, check=True)
        print("  ✓ Dependências instaladas com sucesso!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Erro ao instalar: {e}\n")
        return False

def verify_installation():
    print("[4/4] Verificando instalação...")
    
    modules = ['psutil', 'colorama', 'requests', 'dotenv']
    
    for module in modules:
        try:
            __import__(module)
            print(f"  ✓ {module} OK")
        except ImportError:
            print(f"  ✗ {module} não encontrado")
            return False
    
    print("\n" + "="*50)
    print("  ✅ Instalação Completa!")
    print("="*50)
    print("\nExecute: python main.py\n")
    return True

def main():
    print_header()
    
    if not check_python():
        print("Atualize Python em: https://www.python.org")
        return False
    
    if not check_pip():
        print("Instale pip com: python -m ensurepip --upgrade")
        return False
    
    if not install_dependencies():
        print("Tente instalar manualmente: pip install -r requirements.txt")
        return False
    
    if not verify_installation():
        return False
    
    return True

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelado pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Erro: {e}")
        sys.exit(1)
