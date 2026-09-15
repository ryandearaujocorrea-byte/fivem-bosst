# 📦 Guia de Instalação - FiveM PC Booster

## 🚀 Instalação Rápida

### Windows

1. **Baixe Python 3.8+**
   - Acesse: https://www.python.org/downloads/
   - Selecione a versão mais recente
   - **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação

2. **Clone o repositório**
   ```bash
   git clone https://github.com/ryandearaujocorrea-byte/fivem-bosst.git
   cd fivem-bosst
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute**
   - Opção 1 (Duplo clique): `run-fivem-bosst.bat`
   - Opção 2 (Prompt): `python main.py`

### Linux/macOS

1. **Instale Python**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip
   
   # macOS (com Homebrew)
   brew install python3
   ```

2. **Clone o repositório**
   ```bash
   git clone https://github.com/ryandearaujocorrea-byte/fivem-bosst.git
   cd fivem-bosst
   ```

3. **Instale as dependências**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Dê permissão de execução**
   ```bash
   chmod +x run-fivem-bosst.sh
   ```

5. **Execute**
   - Opção 1: `./run-fivem-bosst.sh`
   - Opção 2: `python3 main.py`

## ⚠️ Privilégios de Administrador

Algumas otimizações requerem privilégios elevados:

### Windows
- Clique com botão direito no `run-fivem-bosst.bat`
- Selecione "Executar como administrador"

### Linux/macOS
```bash
sudo python3 main.py
```

## 🔧 Solução de Problemas

### "Python não encontrado"
- Verifique se Python está instalado: `python --version`
- Se não, baixe em: https://www.python.org
- Reinicie o terminal após instalar

### "Module not found"
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### "Permission denied" (Linux/macOS)
```bash
chmod +x run-fivem-bosst.sh
```

### "psutil not found"
```bash
pip install psutil
```

## 📋 Dependências

- **psutil** - Monitoramento de sistema
- **Flask** - (não usado neste projeto)
- **colorama** - Cores no terminal
- **requests** - Requisições HTTP
- **python-dotenv** - Variáveis de ambiente
- **PyQt6** - (opcional para interface)

## ✅ Verificação de Instalação

```bash
# Verificar Python
python --version

# Verificar pip
pip --version

# Verificar dependências
pip list
```

## 🎯 Próximos Passos

Após instalar:
1. Execute o programa: `python main.py`
2. Escolha "Otimização Completa" no menu
3. Reinicie seu PC
4. Aproveite o aumento de FPS! 🎮
