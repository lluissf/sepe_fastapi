### Instalar a máquina virtual
python3 -m venv .venv
### Habilitar a máquina virtual
source .venv/bin/activate
### Instalar as libs
pip install -r requirements.txt

### Atualizar as libs
pip freeze > requirements.txt

### Rodar o backend (FAST API)
uvicorn main:app --reload
