from sqlalchemy.orm import Session
import models, schemas

# Criar empresa
def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

# Listar todas as empresas
def get_empresas(db: Session):
    return db.query(models.Empresa).all()

# Obter uma empresa por ID
def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

# Excluir uma empresa pelo ID
def delete_empresa(db: Session, empresa_id: int):
    empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if empresa:
        db.delete(empresa)
        db.commit()
    return empresa

# Criar obrigação acessória
def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

# Listar obrigações acessórias de uma empresa
def get_obrigacoes_by_empresa(db: Session, empresa_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.empresa_id == empresa_id).all()
