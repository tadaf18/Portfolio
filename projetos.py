import streamlit as st

def run():
    # CSS para as tags de habilidade e para o "card" do projeto
    # (Removi o CSS das imagens)
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
    .project-container {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1.5em;
        transition: all 0.3s ease-in-out;
        height: 100%; /* Garante que as colunas tenham a mesma altura */
    }
    .project-container:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-color: #0A66C2;
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader('Projetos de Ciência de Dados')
    st.write("Aqui estão alguns projetos que demonstram minhas habilidades em análise, modelagem e visualização de dados.")
    st.write("---")

    col1, col2 = st.columns(2)

    # --- Projeto 1: Unicórnios ---
    with col1:
        with st.container(border=False):
            st.markdown('<div class="project-container">', unsafe_allow_html=True)
            
            # 1. Título (Mais chamativo, com emoji)
            st.markdown("### 🦄 Decifrando os Unicórnios")
            
            # 2. Descrição Curta (Focada no objetivo)
            st.write("Análise exploratória (EDA) para identificar os **fatores-chave** (setor, país, investidores) por trás dos *valuations* bilionários.")

            # 3. Tags de Ferramentas (Palavras-chave)
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Pandas</span>'
                '<span class="project-tag">EDA</span>'
                '<span class="project-tag">Seaborn</span>'
                '<span class="project-tag">Kaggle Dataset</span>',
                unsafe_allow_html=True
            )
            
            st.write("") # Espaçamento

            # 4. Botão de Ação
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/case-unicornios")

            # 5. O Storytelling (dentro do expander)
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** O que faz uma startup atingir o status de "Unicórnio"? Quais são os fatores comuns (setor, país, investidores) por trás dessas empresas de rápido crescimento?
                - **Método:** Utilizei Pandas para limpeza e transformação dos dados. Realizei uma Análise Exploratória de Dados (EDA) e criei visualizações com Seaborn e Matplotlib para identificar tendências, mapear geograficamente os unicórnios e analisar os *valuations* por setor.
                - **Insights:** A análise revelou que 'Fintech' e 'E-commerce' são os setores dominantes. Os EUA e a China concentram a grande maioria dos unicórnios, mas investidores como 'Sequoia Capital' e 'Tiger Global Management' têm um portfólio global diversificado.
                """)
            
            st.markdown('</div>', unsafe_allow_html=True) # Fecha o container


    # --- Projeto 2: Desempenho de Alunos ---
    with col2:
        with st.container(border=False):
            st.markdown('<div class="project-container">', unsafe_allow_html=True)
            
            # 1. Título (Mais chamativo, com emoji)
            st.markdown("### 🎓 Fatores de Sucesso Acadêmico")
            
            # 2. Descrição Curta (Focada no método e objetivo)
            st.write("Investigação com **Regressão Linear** para medir como fatores socioeconômicos (alimentação, pais) impactam as notas dos alunos.")

            # 3. Tags de Ferramentas (Palavras-chave)
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Regressão Linear</span>'
                '<span class="project-tag">Scikit-learn</span>'
                '<span class="project-tag">Teste de Hipótese</span>'
                '<span class="project-tag">NumPy</span>',
                unsafe_allow_html=True
            )

            st.write("") # Espaçamento

            # 4. Botão de Ação
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/Portfolio/blob/main/Projeto_Estudantes.ipynb")

            # 5. O Storytelling (dentro do expander)
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Quais fatores têm o maior impacto no desempenho acadêmico dos alunos? A preparação pré-teste é mais influente que o nível educacional dos pais?
                - **Método:** Apliquei testes de hipótese (Teste-T) para comparar grupos. Construí um modelo de **Regressão Linear Múltipla** com Scikit-learn para identificar quais variáveis melhor predizem a nota final de matemática.
                - **Insights:** O modelo de regressão mostrou que "concluir o curso de preparação para o teste" e "status de alimentação" foram os preditores mais significativos, tendo um impacto maior no desempenho do que o nível educacional dos pais.
                """)
            
            st.markdown('</div>', unsafe_allow_html=True) # Fecha o container

# Esta parte é para testar o arquivo isoladamente
if __name__ == "__main__":
    run()
