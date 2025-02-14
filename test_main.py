
import pytest
from fastapi.testclient import TestClient
from main import app
from crud import delete_empresa  # Importa a função de limpar o banco
import models
from sqlalchemy.orm import Session
from database import SessionLocal 

client = TestClient(app)

# Fixture para obter a sessão do banco de dados
@pytest.fixture(scope="function")
def db():
    db = SessionLocal()  # Cria a sessão do banco de dados
    yield db  # Passa a sessão do banco de dados para o teste
    db.close()  # Fecha a sessão após o teste

# Fixture que garante a limpeza do banco de dados antes e depois dos testes
@pytest.fixture(scope="function", autouse=True)
def limpar_empresas(db: Session):
    # Limpa todas as empresas antes do teste
    empresas = db.query(models.Empresa).all()  # Busca todas as empresas
    for empresa in empresas:
        delete_empresa(db, empresa.id)  # Passa o ID de cada empresa para deletar

    yield  # Aqui o teste será executado

    # Limpa novamente após o teste
    empresas = db.query(models.Empresa).all()  # Busca todas as empresas
    for empresa in empresas:
        delete_empresa(db, empresa.id)  # Passa o ID de cada empresa para deletar

# Função para criar uma empresa antes do teste de listagem
def create_empresa():
    return client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000195",
        "endereco": "Rua Teste, 123",
        "email": "teste@empresa.com",
        "telefone": "123456789"
    })

# Testar criação de empresa
def test_create_empresa():
    response = client.post("/empresas/", json={"nome": "Empresa Teste", "cnpj": "12345678000195", "endereco": "Rua Teste, 123", "email": "teste@empresa.com", "telefone": "123456789"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

# Testar listagem de empresas
def test_list_empresas():
    # Cria uma empresa antes de listar
    create_empresa()

    response = client.get("/empresas/")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica que pelo menos uma empresa foi retornada

# Testar obter empresa por ID
def test_get_empresa():
    response = client.post("/empresas/", json={"nome": "Empresa Teste", "cnpj": "12345678000195", "endereco": "Rua Teste, 123", "email": "teste@empresa.com", "telefone": "123456789"})
    empresa_id = response.json()["id"]
    
    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    assert response.json()["id"] == empresa_id

# Testar criação de obrigação acessória
def test_create_obrigacao():
    # Criar empresa antes
    response_empresa = client.post("/empresas/", json={"nome": "Empresa Teste", "cnpj": "12345678000195", "endereco": "Rua Teste, 123", "email": "teste@empresa.com", "telefone": "123456789"})
    empresa_id = response_empresa.json()["id"]

    response = client.post("/obrigacoes/", json={"nome": "Declaração Anual", "periodicidade": "anual", "empresa_id": empresa_id})
    assert response.status_code == 200
    assert response.json()["nome"] == "Declaração Anual"

# Testar listagem de obrigações acessórias de uma empresa
def test_list_obrigacoes():
    # Criar empresa antes
    response_empresa = client.post("/empresas/", json={"nome": "Empresa Teste", "cnpj": "12345678000195", "endereco": "Rua Teste, 123", "email": "teste@empresa.com", "telefone": "123456789"})
    empresa_id = response_empresa.json()["id"]
    
    # Criar obrigação
    client.post("/obrigacoes/", json={"nome": "Declaração Anual", "periodicidade": "anual", "empresa_id": empresa_id})
    
    response = client.get(f"/empresas/{empresa_id}/obrigacoes")
    assert response.status_code == 200
    assert len(response.json()) > 0  
