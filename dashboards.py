import streamlit as st
import os
from pathlib import Path

# ===============================
# FUNÇÃO DE AJUDA PARA NAVEGAÇÃO
# ===============================
def change_page_local(page_name):
    st.session_state.page = page_name


def run():
    # ========= CSS das tags =========
    st.markdown("""
    <style>
    .project-tag {
        display: inline-block;
        padding: 0.25em 0.6em;
        font-size: 0.75em;
        font-weight: 600;
        line-height: 1;
        color: #0A66C2;
        background-color: #E7F0F8;
        border-radius: 0.25rem;
        margin-right: 0.3em;
        margin-bottom: 0.3em;
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("📊 Dashboards Interativos (Power BI)")
    st.write("Visualize abaixo os dashboards desenvolvidos e baixe os arquivos originais para análise no Power BI.")
    st.write("---")

    # Caminhos dos arquivos locais (.pbix)
    arquivos = {
        "Logística": "Análise de Dados de Logística.pbix",
        "RH": "Análise de Dados de RH.pbix",
        "Comercial": "Dashboard Comercial - Performance de venda.pbix",
        "Financeiro": "Dashboard de Análise Financeira.pbix"
    }

    # ===============================
    # PRIMEIRA LINHA DE DASHBOARDS
    # ===============================
    col1, col2 = st.columns(2)

    # ----- Dashboard Logística -----
    with col1:
        with st.container(border=True):
            st.markdown("### 🚚 Análise de Dados de Logística (Power BI)")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Logística</span>'
                '<span class="project-tag">KPIs</span>',
                unsafe_allow_html=True
            )

            img_path = "imagens/logistica.png"
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning("⚠️ Imagem do dashboard de Logística não encontrada.")

            if os.path.exists(arquivos["Logística"]):
                with open(arquivos["Logística"], "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(arquivos["Logística"]).name)
            else:
                st.error("Arquivo Power BI não encontrado.")

    # ----- Dashboard RH -----
    with col2:
        with st.container(border=True):
            st.markdown("### 👥 Dashboard de RH (Power BI)")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">RH</span>'
                '<span class="project-tag">KPIs</span>',
                unsafe_allow_html=True
            )

            img_path = "imagens/rh.png"
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning("⚠️ Imagem do dashboard de RH não encontrada.")

            if os.path.exists(arquivos["RH"]):
                with open(arquivos["RH"], "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(arquivos["RH"]).name)
            else:
                st.error("Arquivo Power BI não encontrado.")

    st.write("---")

    # ===============================
    # SEGUNDA LINHA DE DASHBOARDS
    # ===============================
    col3, col4 = st.columns(2)

    # ----- Dashboard Comercial -----
    with col3:
        with st.container(border=True):
            st.markdown("### 💼 Dashboard Comercial - Performance de Vendas")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Comercial</span>'
                '<span class="project-tag">Vendas</span>',
                unsafe_allow_html=True
            )

            img_path = "imagens/comercial.png"
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning("⚠️ Imagem do dashboard Comercial não encontrada.")

            if os.path.exists(arquivos["Comercial"]):
                with open(arquivos["Comercial"], "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(arquivos["Comercial"]).name)
            else:
                st.error("Arquivo Power BI não encontrado.")

    # ----- Dashboard Financeiro -----
    with col4:
        with st.container(border=True):
            st.markdown("### 💰 Dashboard Financeiro (Power BI)")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Financeiro</span>'
                '<span class="project-tag">DRE</span>',
                unsafe_allow_html=True
            )

            img_path = "imagens/financeiro.png"
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning("⚠️ Imagem do dashboard Financeiro não encontrada.")

            if os.path.exists(arquivos["Financeiro"]):
                with open(arquivos["Financeiro"], "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(arquivos["Financeiro"]).name)
            else:
                st.error("Arquivo Power BI não encontrado.")

    st.write("---")

    # ===============================
    # BOTÕES DE NAVEGAÇÃO
    # ===============================
    st.markdown("##### Navegar para:")
    col_nav1, col_nav2, col_nav3 = st.columns(3)

    with col_nav1:
        st.button(
            "🏠 Início",
            on_click=change_page_local,
            args=['Início'],
            use_container_width=True
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


# ===============================
# EXECUÇÃO ISOLADA PARA TESTES
# ===============================
if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 'Dashboards'
    run()
    st.write(f"Página atual no session_state: {st.session_state.page}")
