#Otros
from flask_security import UserMixin, RoleMixin

#Para la creacion de la TABLA
from utils.database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                    String, ForeignKey, UnicodeText, Text

class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    permissions = Column(UnicodeText)

    def __str__(self) -> str:
        return self.name

class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    id_armados = relationship('Armados', backref='user')
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    tecnico = relationship('Tecnico', backref='user')

    def __str__(self) -> str:
        return self.username

class Tecnico(Base):
    __tablename__ = 'tecnico'
    id = Column(Integer, primary_key=True)
    link_profesional = Column(String(255), unique=True, nullable=False)
    titulo = Column(String(255), nullable=False)
    descripcion_perfil = Column(Text())
    activo = Column(Boolean())
    user_id= Column('user_id', Integer(), ForeignKey('user.id'))

    def __init__(self,link_profesional,titulo,descripcion_perfil,user_id):
        self.link_profesional = link_profesional
        self.titulo = titulo
        self.descripcion_perfil = descripcion_perfil
        self.user_id = user_id

    def __str__(self) -> str:
        return  "Titulo alcanzado: " + self.titulo       