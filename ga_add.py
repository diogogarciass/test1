import streamlit as st
import sqlite3
import streamlit_shadcn_ui as ui
import datetime
import pandas as pd

# Conectar ao banco de dados (ou criar um novo arquivo de banco de dados)
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Criar a tabela se ela ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        idade INTEGER,
        profissao TEXT
    )
''')
conn.commit()

consulta = "SELECT * FROM usuarios"
df_usuarios = pd.read_sql_query(consulta, conn)


def display_content():
    # Interface do Streamlit
    st.title("Adicionar Nova Ação")

    # Lista de opções para o dropdown
    opcoes_profissao = ["Engenheiro", "Médico",
                        "Professor", "Estudante", "Outro"]
    opcoes_acao = ["Compras", "Manutenção", "Produção"]
    opcoes_classificao = ["Projeto", "Melhoria"]

    # Formulário para entrada de dados
    with st.form("formulario_dados"):

        tipo_acao = st.selectbox("Tipo Ação", opcoes_acao)
        classificacao = st.selectbox("Classificação", opcoes_classificao)
        descricao = st.text_input("Descrição")
        data_prazo = st.date_input("data", value=None)
        ui.textarea
        # Dropdown para selecionar a profissão
        profissao = st.selectbox("Profissão", opcoes_profissao)
        submit_button = st.form_submit_button("Inserir Dados")

        st.table(df_usuarios)
    # Inserir os dados ao clicar no botão
    if submit_button:
        if tipo_acao and tipo_acao:  # Verificar se os campos obrigatórios estão preenchidos
            cursor.execute("INSERT INTO usuarios (nome, email, idade, profissao) VALUES (?, ?, ?, ?)",
                           (tipo_acao, tipo_acao, 1, tipo_acao))
            conn.commit()
            st.success("Dados inseridos com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

    # Exibir os dados inseridos
    st.subheader("Dados Inseridos")
    dados = cursor.execute("SELECT * FROM usuarios").fetchall()
    for linha in dados:
        st.write(linha)

    # Fechar a conexão ao encerrar o app (opcional)


def close_connection():
    conn.close()
