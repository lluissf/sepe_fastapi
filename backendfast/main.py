from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Modelo de dados para Produto
class Produto(BaseModel):
    id: int
    nome: str
    preco: float

# Simulação de um banco de dados de produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
]

ultimo_id:int = 5
# Rota raiz
@app.get("/")
def hello():
    return {"message": "Hello World"}

# Listar todos os produtos
@app.get("/produtos")
def listar_produtos():
    return produtos

# Obter detalhes de um produto específico
@app.get("/produtos/{produto_id}", response_model=Produto)
def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}

#Adicionar um novo produto
#@app.post("/produtos", response_model=Produto)
#def adicionar_produto(produto: Produto):
#    produtos.append(produto.dict())
#    return produto

# Adicionar um novo produto
@app.post("/produtos/")
def criar_produto(nome: str, preco: float):
    global ultimo_id
    ultimo_id += 1
    novo_produto = {"id": ultimo_id, "nome": nome, "preco": preco}
    produtos.append(novo_produto)
    return novo_produto
