import streamlit as st

def run():
    # ETAPA 1: Copiamos o CSS de tags do arquivo projetos.py
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

    st.subheader("Dashboards Interativos")
    st.write(
        "Aqui estão alguns dos dashboards que criei para análise de dados. "
        "Clique no botão para explorar o relatório interativo."
    )
    st.write("---")

    # --- Primeira Linha de Dashboards ---
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### Análise de Vendas (Power BI)")
            st.write(
                "Dashboard focado em KPIs de vendas, performance de produtos e análise regional. "
                "Criado com Power BI."
            )
            
            # ETAPA 2: Adicionamos as tags
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Vendas</span>'
                '<span class="project-tag">KPIs</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            
            st.link_button("Ver Dashboard Interativo", "#") 

    with col2:
        with st.container(border=True):
            st.markdown("### Dashboard de RH (Tableau)")
            st.write(
                "Análise de métricas de RH, incluindo headcount, diversidade e taxas de turnover. "
                "Criado com Tableau."
            )
            
            # ETAPA 2: Adicionamos as tags
            st.markdown(
                '<span class="project-tag">Tableau</span>'
                '<span class="project-tag">RH</span>'
                '<span class="project-tag">Headcount</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            
            st.link_button("Ver Dashboard Interativo", "#")

    st.write("---") # Linha divisória

    # --- Segunda Linha de Dashboards (Exemplo) ---
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container(border=True):
            st.markdown("### Dashboard Financeiro (Excel)")
            st.write(
                "Análise de DRE, fluxo de caixa e principais indicadores financeiros da companhia."
            )
            
            # ETAPA 2: Adicionamos as tags
            st.markdown(
                '<span class="project-tag">Excel</span>'
                '<span class="project-tag">Financeiro</span>'
                '<span class="project-tag">DRE</span>',
                unsafe_allow_html=True
            )
            st.write("") # Espaçamento
            
            st.link_button("Ver Relatório", "#") 

    with col4:
        pass # Deixando a coluna 4 vazia

# Esta parte é para testar o arquivo isoladamente
if __name__ == "__main__":
    run()
