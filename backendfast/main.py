from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
]

@app.get("/produtos")
def listar_produtos():
    return produtos
@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}