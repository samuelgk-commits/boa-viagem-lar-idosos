# Lar Boa Viagem

> Sistema web para gestão de uma Instituição de Longa Permanência para Idosos (ILPI), desenvolvido em Flask para cadastro e gerenciamento de hóspedes, controle de usuários e organização de quartos.


##  Visão Geral

O **Lar Boa Viagem** é um projeto acadêmico e de portfólio que centraliza as operações administrativas de um lar de idosos, oferecendo uma interface simples e funcional para diferentes níveis de acesso (ADM, Gestor, Cuidador).

Principais objetivos:
- Facilitar rotinas administrativas da ILPI
- Centralizar informações de hóspedes, quartos e usuários
- Oferecer controle de acesso baseado em cargos
- Possibilitar empacotamento em executável (.exe) para distribuição


##  Tecnologias

- Python 
- Flask
- Jinja2
- MySQL
- HTML5 / CSS3 / JavaScript
- PyInstaller (para gerar .exe)


##  Perfis de Usuário

- **Administrador (ADM)** — controle total do sistema e gerenciamento de usuários.
- **Gestor** — gerencia hóspedes, quartos e setores.
- **Cuidador** — acessa informações permitidas pelo seu papel (visualização).


##  Funcionalidades Principais

- Autenticação por cargo e controle de sessão
- CRUD de hóspedes
- Organização e cadastro de quartos/setores
- Templates com Jinja2
- Versão empacotada em executável (PyInstaller)


## Estrutura do Projeto

```bash
├── Database/        # Modelos e conexão com o banco de dados
├── routes/          # Rotas organizadas por módulo (adm, gestor, cuidador...)
├── static/          # CSS, imagens, JS
├── templates/       # Templates Jinja2
├── main.py          # Entrada da aplicação
├── configuration.py # Configurações (DB, secret key, etc.)
├── utils.py         # Funções utilitárias (ex.: validar_adm)
├── utils_db.py      # Funções/utilitários de DB
├── icon.ico
├── README.md
└── .gitignore
```


##  Instalação (Desenvolvimento)

- Um adendo importante é que sempre que for sair do app saia pelo botão de sair na pagina de login, caso contrário o main ficara rodando em segundo plano no seu dispositivo oque pode ser incoveniênte para voçê


### 1. Clonar repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-repositorio
```

### 2. Criar e ativar virtualenv

**Windows**:
```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

**Desativar venv**:
```bash
deactivate
```

> Dica: se ao fechar o terminal o venv "desativa", isso é esperado: você precisa ativá-lo em cada nova sessão (ou configurar o interpretador do seu editor, ex. VS Code, para usar o venv automaticamente).

**import necessarios**

pip install Flask sqlite PyInstaller peewee


### 3. Rodar a aplicação

Com o venv ativo e variáveis configuradas:

```bash
# opção 1 (se main.py inicializa app diretamente, caso esteja em desenvolvimento apenas tire o if do main.py que ele não iniciara a cada alteração)
python main.py 


# opção 2 (se estiver usando flask CLI)
export FLASK_APP=main.py
flask run
```

Acesse `http://127.0.0.1:5000`.


## Empacotar com PyInstaller 

Gerar executável para Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" --icon=icon.ico main.py
```

Observações:
- Ajuste `--add-data` conforme os caminhos do seu SO (no Windows separar com `;`, no Linux/macOS usar `:`).
- Teste o executável em uma máquina limpa para verificar dependências estáticas (templates, static, arquivos de configuração).
- No caso de querer implementar o mysql, ou outros bancos, confirme que as tabelas estão identicas aos models, caso esteja só mudar no Database/database.py.


##  Solução de Problemas Comuns

- **Venv "some" ao fechar terminal**: ative novamente ao abrir uma nova sessão. Configure o IDE/editor para usar o interpretador do venv automaticamente (ex.: VS Code: `Python: Select Interpreter`).

- **Alterações em templates não aparecem**: limpe cache do navegador (Ctrl+F5) e certifique-se de que `debug=True` está ativado durante desenvolvimento para auto-reload. Caso tenha usado a versão .exe certifiquese de fechar com o botão na tela de login, ela pode rodar em segundo plano(oque pode ser visto no gerenciador de tarefas) isso pode interferir no flask identiifcar o codigo correto.

- **Erro de conexão com MySQL**: verifique host/porta/usuário/senha e se o serviço MySQL está em execução. Teste a conexão com um cliente (MySQL Workbench ou `mysql` CLI).

- **Rotas não atualizam**: confirme que você está executando a versão atual do código e que não há múltiplas instâncias rodando na mesma porta.


## Licença

Este projeto está licenciado sob a licença **MIT**.

## Contato

Se quiser, me mande o código ou trechos específicos (ex.: `main.py`, `configuration.py` ou exemplos de rotas) nesse numero (47)991910356 que eu te ajudo a ajustar e configurar para rodar corretamente.



