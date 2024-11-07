import streamlit as st
import ga_add  # Importa o conteúdo do arquivo a1.py
import ga_lista  # Importa o conteúdo do arquivo b1.py


# CSS para aumentar o tamanho do campo de entrada
LOGO = "images/logo.png"


st.logo(LOGO, size="large")


# Sidebar com o selectbox para navegação
st.sidebar.title("Navegação")
option = st.sidebar.selectbox("Selecione uma página:", [
                              "Página A1", "Página B1"])

# Carrega o conteúdo baseado na seleção
if option == "Página A1":
    ga_add.display_content()  # Chama a função para exibir o conteúdo de a1.py
elif option == "Página B1":
    ga_lista.display_content()  # Chama a função para exibir o conteúdo de b1.py
