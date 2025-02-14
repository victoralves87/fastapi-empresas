from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String, nullable=True)
    email = Column(String, nullable=True)
    telefone = Column(String, nullable=True)

    # Relacionamento com ObrigacaoAcessoria, incluindo a exclusão em cascata
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa", cascade="all, delete")

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)  # Exemplo: mensal, trimestral, anual
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    empresa = relationship("Empresa", back_populates="obrigacoes")
