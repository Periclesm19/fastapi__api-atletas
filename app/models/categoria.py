from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Categoria(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(Integer, unique=True, index=True)