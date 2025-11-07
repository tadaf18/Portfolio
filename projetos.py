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
            # DESCRIÇÃO CORRIGIDA
            st.write("Análise exploratória (EDA) do mercado de startups 'Unicórnio' para identificar os **fatores-chave** (setor, país, investidores) por trás dos *valuations* bilionários.")
            # TAGS CORRIGIDAS
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Pandas</span>'
                '<span class="project-tag">EDA</span>'
                '<span class="project-tag">Seaborn</span>'
                '<span class="project-tag">Matplotlib</span>'
                '<span class="project-tag">Fintech</span>'
                '<span class="project-tag">Visualização de Dados</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/case-unicornios")

            # EXPANDER CORRIGIDO
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** O que faz uma startup atingir o status de "Unicórnio" (valorização acima de US$ 1 bilhão)? Quais são os fatores comuns (setor, país, investidores) por trás dessas empresas?
                - **Método:** Utilização da biblioteca Pandas para limpeza e transformação dos dados. Realização de uma Análise Exploratória de Dados (EDA) e criação de visualizações com Seaborn e Matplotlib para identificar tendências e mapear geograficamente os unicórnios.
                - **Insights:** A maior concentração de unicórnios está nos **Estados Unidos** (51.4%) e na **China** (10.1%). Os setores com maior número são **Fintech**, **Internet software & services** e **E-commerce & direct-to-consumer**.
                """)

    # --- Projeto 2: Desempenho de Alunos ---
    with col2:
        with st.container(border=True):
            # TÍTULO E DESCRIÇÃO CORRIGIDOS
            st.markdown("### 📚 Fatores de Desempenho Escolar")
            st.write("Estudo das **variáveis preditoras** do desempenho (notas) de estudantes, com foco na influência de fatores sociodemográficos e preparação para testes.")
            # TAGS CORRIGIDAS
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Scikit-learn</span>'
                '<span class="project-tag">Regressão Linear</span>'
                '<span class="project-tag">Modelagem Preditiva</span>'
                '<span class="project-tag">Estatística</span>'
                '<span class="project-tag">Seaborn</span>'
                '<span class="project-tag">Teste de Hipótese</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/Projeto-Estudantes.git")

            # EXPANDER CORRIGIDO
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Quais fatores (gênero, etnia, nível educacional dos pais, tipo de almoço, curso preparatório) têm o **maior impacto** no desempenho dos alunos?
                - **Método:** Realização de **EDA** com Boxplots e Pairplots. Utilização de **Testes de Hipótese (Teste-T)** para análise de diferenças de grupos. Construção de um modelo de **Regressão Linear Múltipla** com Scikit-learn.
                - **Insights:** O modelo de regressão mostrou que "**concluir o curso de preparação para o teste**" e "**status de alimentação (lunch)**" foram os preditores mais significativos, superando o nível educacional dos pais.
                """)

    # --- Projeto 3: Mercado Financeiro ---
    # CORREÇÃO DE LAYOUT: Usando col1 (em vez do col3 inexistente)
    with col1:
        with st.container(border=True):
            # TÍTULO E DESCRIÇÃO CORRIGIDOS
            st.markdown("### 📈 Mercado Financeiro - Séries Temporais (MGLU3)")
            st.write("Análise de Séries Temporais do valor de fechamento das ações da Magazine Luiza (MGLU3), incluindo médias móveis, tendências e sazonalidade.")
            # TAGS CORRIGIDAS
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Pandas</span>'
                '<span class="project-tag">Séries Temporais</span>'
                '<span class="project-tag">Mercado Financeiro</span>'
                '<span class="project-tag">Matplotlib</span>'
                '<span class="project-tag">Plotly</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/projeto_mercado_financeiro/tree/main")

            # EXPANDER CORRIGIDO
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Analisar o comportamento histórico (Série Temporal) do valor de fechamento das ações da MGLU3 para identificar tendências, volatilidade e sazonalidade.
                - **Método:** Uso de Pandas para transformar os dados em uma série temporal. Cálculo e plotagem de **Médias Móveis** (5 e 30 dias). Análise da distribuição de preços por mês (Boxplot Mensal) para verificar sazonalidade.
                - **Insights:** A análise das Médias Móveis (5 e 30 dias) permite identificar a tendência principal e a volatilidade do preço da ação. O Boxplot Mensal pode revelar períodos de maior ou menor volatilidade.
                """)

    # --- Projeto 4: Mercado de Games ---
    # CORREÇÃO DE LAYOUT: Usando col2 (em vez do col4 inexistente)
    with col2:
        with st.container(border=True):
            # TÍTULO E DESCRIÇÃO CORRIGIDOS
            st.markdown("### 🎮 Análise do Mercado de Games (PS4)")
            st.write("Análise da distribuição global de vendas de jogos de PlayStation 4 (PS4), com foco em tendências regionais, gêneros e editores mais lucrativos.")
            # TAGS CORRIGIDAS
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Pandas</span>'
                '<span class="project-tag">Análise Exploratória</span>'
                '<span class="project-tag">Seaborn</span>'
                '<span class="project-tag">Mercado de Games</span>'
                '<span class="project-tag">Label Encoding</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/projeto_mercado_de_games/tree/main")

            # EXPANDER CORRIGIDO
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Entender as tendências do mercado de games para PS4, analisando a distribuição das vendas globais por ano, região (América do Norte, Europa) e categoria (gênero e editor).
                - **Método:** Uso de Pandas para limpeza e transformação. Análise estatística e criação de gráficos de barras e distribuição (KDE). Conversão de variáveis categóricas para numéricas usando `LabelEncoder`.
                - **Insights:** O pico de vendas global para PS4 ocorreu em **2016**. A **Europa** e a **América do Norte** são os mercados mais relevantes. Os gêneros **Action** e **Shooter** estão entre os mais vendidos.
                """)

    # --- Projeto 5: RH ---
    # CORREÇÃO DE LAYOUT: Usando col1 (em vez do col5 inexistente)
    with col1:
        with st.container(border=True):
            # TÍTULO E DESCRIÇÃO CORRIGIDOS
            st.markdown("### 🧑‍💼 Tempo de Experiência vs Salário (RH)")
            st.write("Modelagem de Regressão Linear Simples para prever o Salário (Renda) com base no Tempo de Experiência (Xp) para auxiliar na gestão de RH.")
            # TAGS CORRIGIDAS
            st.markdown(
                '<span class="project-tag">Python</span>'
                '<span class="project-tag">Regressão Linear</span>'
                '<span class="project-tag">Modelagem Preditiva</span>'
                '<span class="project-tag">Recursos Humanos (RH)</span>'
                '<span class="project-tag">Scikit-learn</span>'
                '<span class="project-tag">EDA</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            st.link_button("Ver Projeto no GitHub", "https://github.com/tadaf18/projeto_mercado_de_games") # Mantido link original

            # EXPANDER CORRIGIDO
            with st.expander("Ver detalhes da análise"):
                st.markdown("""
                - **Problema:** Analisar a correlação entre Anos de Experiência e Salário e construir um modelo preditivo que permita estimar a remuneração com base na experiência.
                - **Método:** Análise descritiva e visualização da distribuição das variáveis. Aplicação de um modelo de **Regressão Linear Simples** usando Scikit-learn para modelar a relação.
                - **Insights:** O modelo demonstra uma **forte correlação linear positiva** entre o tempo de experiência e o salário, podendo ser usado para prever salários com base na experiência.
                """)
    
    # ===============================
    # BOTÕES DE NAVEGAÇÃO DE PÁGINA
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
    if 'page' not in st.session_state:
        st.session_state.page = 'Projetos'
    run()
