from fastapi import FastAPI
app = FastAPI()

# Simulação de um banco de dados de produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
]
# Rota raiz
@app.get("/")
def hello():
    return {"message": "Hello World"}

# Listar todos os produtos
@app.get("/produtos")
def listar_produtos():
    return produtos

# Obter detalhes de um produto específico
@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}