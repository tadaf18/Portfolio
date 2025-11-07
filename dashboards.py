import streamlit as st

# ===============================
# FUNÇÃO DE AJUDA PARA NAVEGAÇÃO
# ===============================
# Esta função altera o valor no session_state
def change_page_local(page_name):
    st.session_state.page = page_name

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
            st.markdown("### Análise de Dados Logística (Power BI)")
            
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Logística</span>'
                '<span class="project-tag">KPIs</span>',
                unsafe_allow_html=True
            )
            st.write("") 
            
            st.link_button("Ver Dashboard Interativo", "https://drive.google.com/file/d/1anZoPwS8kuvP294ZHI7Phcep6ENmJ-Dn/view?usp=drive_link") 

    with col2:
        with st.container(border=True):
            st.markdown("### Dashboard de RH (Power BI)")
            
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">RH</span>'
                '<span class="project-tag">KPIs</span>',
                unsafe_allow_html=True
            )
            st.write("") 
            
            st.link_button("Ver Dashboard Interativo", "https://drive.google.com/file/d/1wSZraDomgOW8FTuRmEJVXsaeBQdQEFsC/view?usp=drive_link")

    st.write("---") 

    # --- Segunda Linha de Dashboards (Exemplo) ---
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container(border=True):
            st.markdown("### Dashboard Comercial - Performance de venda (Power BI)")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Vendas</span>'
                '<span class="project-tag">Comercial</span>',
                unsafe_allow_html=True
            )
            st.write("") 
            
            st.link_button("Ver Relatório", "https://drive.google.com/file/d/1Ec3yLiNdx957Jo2sgHhX46xlxeRwDO7o/view?usp=drive_link") 

    with col4:
            with st.container(border=True):
                st.markdown("### Dashboard Financeiro (Power BI)")
                st.markdown(
                    '<span class="project-tag">Power BI</span>'
                    '<span class="project-tag">Financeiro</span>'
                    '<span class="project-tag">DRE</span>',
                    unsafe_allow_html=True
                )
                st.write("") 
                
                st.link_button("Ver Relatório", "https://drive.google.com/file/d/1t-3JqUSwYg_Tzo1NOiEM00HsU0QGYvgY/view?usp=drive_link") 	

    # O bloco "with col5:" foi removido pois 'col5' não estava definida.

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
            "💼 Projetos", 
            on_click=change_page_local, 
            args=['Projetos'], 
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
    # Para testar, precisamos simular o st.session_state se ele não existir
    if 'page' not in st.session_state:
        st.session_state.page = 'Dashboards' # Valor inicial de exemplo
    
    run()
    
    # Exibe a página atual (para fins de teste)
    st.write(f"Página atual no session_state: {st.session_state.page}")
