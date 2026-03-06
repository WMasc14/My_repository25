from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Tarefas")

# Modelo de dados
class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

# "Base de dados" em memória
tarefas: List[Tarefa] = []

# Rota inicial
@app.get("/")
def home():
    return {"mensagem": "API de Tarefas a funcionar 🚀"}

# Listar todas as tarefas
@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

# Criar uma nova tarefa
@app.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    for t in tarefas:
        if t.id == tarefa.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    tarefas.append(tarefa)
    return tarefa

# Atualizar tarefa
@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for i, t in enumerate(tarefas):
        if t.id == tarefa_id:
            tarefas[i] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Apagar tarefa
@app.delete("/tarefas/{tarefa_id}")
def apagar_tarefa(tarefa_id: int):
    for i, t in enumerate(tarefas):
        if t.id == tarefa_id:
            tarefas.pop(i)
            return {"mensagem": "Tarefa apagada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
# Executar o servidor com: uvicorn main:app --reload

