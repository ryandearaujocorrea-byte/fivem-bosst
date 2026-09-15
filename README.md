# 🎮 FiveM PC Booster - Otimizador de Performance

Um aplicativo completo em Python para otimizar seu PC e aumentar drasticamente os FPS em FiveM!

## ✨ Funcionalidades

### 🧹 Limpeza de Arquivos
- Limpeza de arquivos temporários
- Limpeza de cache do sistema
- Limpeza de Prefetch do Windows

### ⚙️ Gerenciamento de Processos
- Detecção de processos que consomem recursos
- Encerramento automático de bloatware
- Monitoramento de CPU e memória
- Estatísticas em tempo real

### 🎮 Otimização de GPU
- Detecção automática de GPU (NVIDIA, AMD, Intel)
- Otimizações específicas por fabricante
- Ativação de modo High Performance
- Desabilitação de economia de energia

### 🌐 Otimização de Rede
- Teste de ping
- Otimização de DNS
- Desabilitação de IPv6
- Otimização de TCP/IP
- Redução de latência

### 💾 Gerenciamento de RAM
- Monitoramento de memória
- Otimização de memória virtual
- Gerenciamento de pagefile
- Redução de overhead de sistema

## 🚀 Como Usar

### Pré-requisitos
- Windows 10/11
- Python 3.8+
- Privilégios de Administrador

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ryandearaujocorrea-byte/fivem-bosst.git
cd fivem-bosst
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute como administrador:
```bash
python main.py
```

## 📋 Menu Principal

```
[MENU PRINCIPAL]

1. Análise Rápida do Sistema
   - Mostra uso de CPU, RAM, GPU e Ping

2. Otimização Completa
   - Executa todas as otimizações em sequência

3. Limpeza de Arquivos Temporários
   - Remove arquivos temporários e cache

4. Gerenciar Processos em Background
   - Lista e encerra processos desnecessários

5. Otimizar GPU
   - Aplica otimizações específicas de GPU

6. Otimizar Rede
   - Otimiza DNS, TCP/IP e reduz latência

7. Gerenciar RAM
   - Monitora e otimiza memória

8. Sair
```

## 📊 Processos Bloat Removidos Automaticamente

- OneDrive
- Google Chrome/Crash Handler
- Spotify
- Discord
- Steam
- TeamViewer
- Skype
- uTorrent
- BitTorrent
- AnyDesk
- Telegram
- WhatsApp
- Adobe Creative Cloud
- Antivírus desnecessários

## 🔧 Estrutura do Projeto

```
fivem-bosst/
├── main.py                    # Arquivo principal
├── requirements.txt           # Dependências
├── README.md                  # Este arquivo
└── optimizer/
    ├── __init__.py
    ├── cleaner.py            # Limpeza de arquivos
    ├── process_manager.py    # Gerenciamento de processos
    ├── gpu_optimizer.py      # Otimização de GPU
    ├── network_optimizer.py  # Otimização de rede
    └── ram_manager.py        # Gerenciamento de RAM
```

## ⚠️ Aviso Importante

- **Execute como Administrador**: A maioria das otimizações requer privilégios de admin
- **Faça backup**: Sempre faça backup importante antes de executar otimizações
- **Use com cuidado**: Algumas otimizações alteram configurações de sistema
- **Antivírus**: Seu antivírus pode bloquear algumas operações

## 🎯 Dicas para Melhorar FPS em FiveM

1. **Sempre execute a otimização completa antes de jogar**
2. **Feche aplicativos desnecessários (Discord, Spotify, etc)**
3. **Use este app regularmente** (semanal ou quinzenal)
4. **Reinicie o PC após uma otimização completa**
5. **Mantenha drivers de GPU atualizados**
6. **Ajuste gráficos do FiveM conforme sua GPU**

## 📈 Resultados Esperados

Após usar o FiveM PC Booster, você pode esperar:
- ⬆️ **15-40% de aumento em FPS**
- ⬇️ Redução de stutters e lag
- ⬇️ Melhor tempo de resposta (menor ping)
- ⬇️ Menor consumo de RAM
- ⏱️ Carregamento mais rápido

## 🛠️ Troubleshooting

### "Permission denied"
- Execute o prompt de comando como Administrador
- Execute: `python main.py` com UAC elevado

### "Module not found"
- Reinstale as dependências: `pip install -r requirements.txt`

### Não vejo melhoria em FPS
- Execute "Otimização Completa"
- Reinicie seu PC
- Verifique drivers de GPU
- Feche aplicativos de background

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Fazer pull requests

## 📝 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido com ❤️ para a comunidade FiveM

## 🔗 Links Úteis

- [FiveM Official](https://fivem.net)
- [Python Documentation](https://docs.python.org)
- [Windows Performance Tuning](https://docs.microsoft.com/windows)

---

**Aproveite o jogo com FPS máximo! 🚀🎮**
