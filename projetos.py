import streamlit as st

# Para rodar no terminal: python -m streamlit run main.py

def run():
    st.subheader('Projetos no Github')
    st.write("Aqui estão alguns dos meus projetos em análise de dados no GitHub.")
    st.write("---") # Adiciona uma linha divisória

    col1, col2 = st.columns(2)

    # --- Projeto 1 ---
    with col1:
        st.markdown("### Análise de dados de empresas 'Unicórnios'")
        st.write("Análise de região, setores e valuation.")
        st.link_button("Ver Projeto", "https://github.com/tadaf18/case-unicornios")

    # --- Projeto 2 (Exemplo) ---
    with col2:
        st.markdown("### Análise do conjunto de dados de notas obtidas pelos alunos em várias disciplinas.")
        st.write("Vamos tentar entender a influência dos antecedentes dos pais, preparação para testes etc. no desempenho dos alunos.")
        st.link_button("Ver Projeto", "https://github.com/tadaf18/Portfolio/blob/main/Projeto_Estudantes.ipynb") # Lembre-se de trocar o '#' pelo link do GitHub

    # Você pode adicionar mais colunas ou linhas para mais projetos
    # st.write("---")
    # col3, col4 = st.columns(2)
    # with col3:
    #    st.markdown("### Título do Projeto 3")
    #    ...
