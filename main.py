from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar empresa
@app.post("/empresas/", response_model=schemas.EmpresaResponse)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db, empresa)

# Listar empresas
@app.get("/empresas/", response_model=list[schemas.EmpresaResponse])
def list_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db)

# Obter empresa por ID
@app.get("/empresas/{empresa_id}", response_model=schemas.EmpresaResponse)
def get_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = crud.get_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

# Deletar empresa
@app.delete("/empresas/{empresa_id}", response_model=schemas.EmpresaResponse)  # Corrigido o modelo de resposta
def delete_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    empresa = crud.delete_empresa(db, empresa_id)  # Corrigindo a chamada para a função de delete
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

# Criar obrigação acessória
@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaResponse)
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao(db, obrigacao)

# Listar obrigações acessórias de uma empresa
@app.get("/empresas/{empresa_id}/obrigacoes", response_model=list[schemas.ObrigacaoAcessoriaResponse])
def list_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return crud.get_obrigacoes_by_empresa(db, empresa_id)
