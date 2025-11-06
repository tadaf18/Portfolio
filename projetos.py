import streamlit as st

# ===============================
# FUNÇÃO DE AJUDA PARA NAVEGAÇÃO
# ===============================
# Esta função altera o valor no session_state
def change_page_local(page_name):
    st.session_state.page = page_name

def run():
    # CSS apenas para as tags de habilidade
    st.markdown("""
    <style>
    .project-tag {
        display: inline-block;
        padding: 0.25em 0.6em;
        font-size: 0.75em;
        font-weight: 600;
        line-height: 1;
        color: #0A66C2; /* Cor principal */
        background-color: #E7F0F8; /* Fundo claro */
        border-radius: 0.25rem;
        margin-right: 0.3em;
        margin-bottom: 0.3em;
    }
    
    </style>
    """, unsafe_allow_html=True)

    st.subheader('Projetos de Ciência de Dados')
    st.write("Aqui estão alguns projetos que demonstram minhas habilidades em análise, modelagem e visualização de dados.")
    st.write("---")

    col1, col2 = st.columns(2)

    # --- Projeto 1: Unicórnios ---
    with col1:
        with st.container(border=True):
            st.markdown("### 🦄 Decifrando os Unicórnios")
            st.write("Análise exploratória (EDA) para identificar os **fatores-chave** (setor, país, investidores) por trás dos *valuations* bilionários.")
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Pandas</span>'
                '<span class="project-tag">EDA</span>'
                '<span class="project-tag">Seaborn</span>'
                '<span class="project-tag">Kaggle Dataset</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/case-unicornios")

            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** O que faz uma startup atingir o status de "Unicórnio"? Quais são os fatores comuns (setor, país, investidores) por trás dessas empresas de rápido crescimento?
                - **Método:** Utilizei Pandas para limpeza e transformação dos dados. Realizei uma Análise Exploratória de Dados (EDA) e criei visualizações com Seaborn e Matplotlib para identificar tendências, mapear geograficamente os unicórnios e analisar os *valuations* por setor.
                - **Insights:** A análise revelou que 'Fintech' e 'E-commerce' são os setores dominantes. Os EUA e a China concentram a grande maioria dos unicórnios, mas investidores como 'Sequoia Capital' e 'Tiger Global Management' têm um portfólio global diversificado.
                """)

    # --- Projeto 2: Desempenho de Alunos ---
    with col2:
        with st.container(border=True):
            st.markdown("### 🎓 Fatores de Sucesso Acadêmico")
            st.write("Investigação com **Regressão Linear** para medir como fatores socioeconômicos (alimentação, pais) impactam as notas dos alunos.")
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Regressão Linear</span>'
                '<span class="project-tag">Scikit-learn</span>'
                '<span class="project-tag">Teste de Hipótese</span>'
                '<span class="project-tag">NumPy</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/Portfolio/blob/main/Projeto_Estudantes.ipynb")

            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Quais fatores têm o maior impacto no desempenho acadêmico dos alunos? A preparação pré-teste é mais influente que o nível educacional dos pais?
                - **Método:** Apliquei testes de hipótese (Teste-T) para comparar grupos. Construí um modelo de **Regressão Linear Múltipla** com Scikit-learn para identificar quais variáveis melhor predizem a nota final de matemática.
                - **Insights:** O modelo de regressão mostrou que "concluir o curso de preparação para o teste" e "status de alimentação" foram os preditores mais significativos, tendo um impacto maior no desempenho do que o nível educacional dos pais.
                """)
    
    # ===============================
    # BOTÕES DE NAVEGAÇÃO DE PÁGINA (NOVO)
    # ===============================
    st.write("---") # Adiciona um separador visual
    st.markdown("##### Navegar para:")

    # Usamos colunas para organizar os botões
    col_nav1, col_nav2, col_nav3 = st.columns(3)

    with col_nav1:
        st.button(
            "🏠 Início", 
            on_click=change_page_local, 
            args=['Início'], 
            use_container_width=True # Faz o botão ocupar a coluna
        )
    
    with col_nav2:
        st.button(
            "📊 Dashboards", 
            on_click=change_page_local, 
            args=['Dashboards'], 
            use_container_width=True
        )

    with col_nav3:
        st.button(
            "📬 Contato", 
            on_click=change_page_local, 
            args=['Contato'], 
            use_container_width=True
        )


# Esta parte é para testar o arquivo isoladamente
if __name__ == "__main__":
    run()
