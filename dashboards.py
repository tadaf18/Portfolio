import streamlit as st

def run():
    st.subheader("Dashboards Interativos")
    st.write(
        "Aqui estão alguns dos dashboards que criei para análise de dados. "
        "Clique no botão para explorar o relatório interativo."
    )
    st.write("---")

    # --- Primeira Linha de Dashboards ---
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Análise de Vendas (Power BI)")
        st.write(
            "Dashboard focado em KPIs de vendas, performance de produtos e análise regional. "
            "Criado com Power BI."
        )
        
        # IMPORTANTE: Troque o '#' pelo link público do seu dashboard
        st.link_button("Ver Dashboard Interativo", "#") 

    with col2:
        st.markdown("### Dashboard de RH (Tableau)")
        st.write(
            "Análise de métricas de RH, incluindo headcount, diversidade e taxas de turnover. "
            "Criado com Tableau."
        )
        
        # IMPORTANTE: Troque o '#' pelo link público do seu dashboard
        st.link_button("Ver Dashboard Interativo", "#")

    st.write("---") # Linha divisória

    # --- Segunda Linha de Dashboards (Exemplo) ---
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### Dashboard Financeiro (Excel)")
        st.write(
            "Análise de DRE, fluxo de caixa e principais indicadores financeiros da companhia."
        )
        # Você pode linkar para um arquivo no OneDrive, Google Drive, etc.
        st.link_button("Ver Relatório", "#") 

    # Deixe a col4 vazia ou adicione outro projeto
    # with col4:
    #    st.markdown("### Título do Projeto")
