# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Introdução a utilização de BD em Python

import sqlite3 #Importando o módulo Sqlite3
con = sqlite3.connect("escola.db") #Criando o BD caso ele não exista
type(con) #Confirmando a conexão

cur = con.cursor() #Criando um cursor (Percorrer os registros)
type(cur)

#Criar uma instrução sql
sql_create = 'create table cursos ' \
'(id integer primary key, '\
'titulo varchar (100), '\
'categoria varchar(140))'

#Executando a instrução sql no cursor
cur.execute(sql_create)

# Criando uma sentenção SQL para inserir registros
sql_insert = 'insert into cursos values (?,?,?)'

# Dados
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for rec in recset:
  cur.execute(sql_insert, rec)

# Grava a transação
con.commit()

# Criando outra sentença SQL para selecionar registros
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

# Mostra
for linha in dados :
  print('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)

# Gerando outros registros
recset = [(1003, 'Gestão de Dados com MongoDB', "Big Data"),
          (1004, 'R Fundamentos', "Análise de Dados")]

# Inserindo os gegistros
for rec in recset:
  cur.execute(sql_insert,rec)

# Gravando a transação
con.commit()

#Seleciona todos so registros
cur.execute(sql_select)

#Recupera os resultados
recset = cur.fetchall()

#Mostra
for rec in recset:
  print('Curso Id: %d, Título: %s, Categoria: %s \n' % rec )

con.close()