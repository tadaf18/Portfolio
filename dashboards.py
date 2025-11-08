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
    # Certifique-se que estes arquivos existem no mesmo diretório do script ou no caminho especificado
    arquivos = {
        "Logística": "Análise de Dados de Logística.pbix",
        "RH": "Análise de Dados de RH.pbix",
        "Comercial": "Dashboard Comercial - Performance de venda.pbix",
        "Financeiro": "Dashboard de Análise Financeira.pbix",
        "Financeiro 2": "Dashboard Financeira.pbix"
    }
    
    # Caminhos das imagens
    # Certifique-se que a pasta "imagens" existe no mesmo diretório do script
    imagens = {
        "Logística": "imagens/logistica.png",
        "RH": "imagens/rh.png",
        "Comercial": "imagens/comercial.png",
        "Financeiro": "imagens/financeiro.png",
        "Financeiro 2": "imagens/financeiro2.png"
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

            img_path = imagens["Logística"]
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"⚠️ Imagem não encontrada: {img_path}")

            file_path = arquivos["Logística"]
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(file_path).name)
            else:
                st.error(f"Arquivo Power BI não encontrado: {file_path}")

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

            img_path = imagens["RH"]
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"⚠️ Imagem não encontrada: {img_path}")

            file_path = arquivos["RH"]
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(file_path).name)
            else:
                st.error(f"Arquivo Power BI não encontrado: {file_path}")

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

            img_path = imagens["Comercial"]
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"⚠️ Imagem não encontrada: {img_path}")

            file_path = arquivos["Comercial"]
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(file_path).name)
            else:
                st.error(f"Arquivo Power BI não encontrado: {file_path}")

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

            img_path = imagens["Financeiro"]
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"⚠️ Imagem não encontrada: {img_path}")

            file_path = arquivos["Financeiro"]
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(file_path).name)
            else:
                st.error(f"Arquivo Power BI não encontrado: {file_path}")
    
    st.write("---") # <--- CORREÇÃO 1: Adicionada linha de separação

    # ===============================
    # TERCEIRA LINHA DE DASHBOARDS 
    # ===============================
    
    # <--- CORREÇÃO 1: Adicionada nova linha de colunas ---
    # O Dashboard "Financeiro 2" estava sendo colocado na col4, junto com o "Financeiro 1".
    # Criei uma nova linha (col5, col6) para ele.
    col5, col6 = st.columns(2)

    # ----- Dashboard Financeiro 2 -----
    with col5: # <--- CORREÇÃO 1: Movido para col5
        with st.container(border=True):
            st.markdown("### 💰 Dashboard Financeiro 2 (Power BI)")
            st.markdown(
                '<span class="project-tag">Power BI</span>'
                '<span class="project-tag">Financeiro</span>'
                '<span class="project-tag">DRE</span>',
                unsafe_allow_html=True
            )

            img_path = imagens["Financeiro 2"]
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                # <--- CORREÇÃO 3: Mensagem de aviso ---
                # A mensagem de aviso da imagem estava incorreta.
                st.warning(f"⚠️ Imagem não encontrada: {img_path}") # Mensagem corrigida

            # <--- CORREÇÃO 2: Caminho do arquivo ---
            # O código estava verificando e abrindo `arquivos["Financeiro"]` em vez de `arquivos["Financeiro 2"]`.
            file_path = arquivos["Financeiro 2"] # Corrigido
            if os.path.exists(file_path):
                with open(file_path, "rb") as f: # Corrigido
                    st.download_button("🔽 Baixar Arquivo (.pbix)", f, file_name=Path(file_path).name)
            else:
                st.error(f"Arquivo Power BI não encontrado: {file_path}")
                
    # A coluna col6 ficará vazia, o que é normal.

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
