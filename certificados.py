import streamlit as st
import os
from pathlib import Path

# ===============================
# FUNÇÃO DE AJUDA PARA NAVEGAÇÃO
# ===============================
# Esta função altera o valor no session_state
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

    st.subheader("🎓 Certificados e Qualificações")
    st.write("Abaixo estão os certificados obtidos. Você pode visualizar a imagem e baixar o PDF original.")
    st.write("---")

    # --- CAMINHOS BASE ---
    PDF_DIR = "certificados/"
    IMG_DIR = "imagens/certificados/"

    # --- LISTA DE CERTIFICADOS ---
    # Os valores aqui devem ser os NOMES EXATOS dos arquivos, sem a extensão .pdf
    certificados = {
        # --- Certificados FM2S ---
        "Liderança em Operações": "Liderança em operações",
        "Liderança em Processos": "Liderança em Processos",
        "Liderança em Qualidade": "Liderança em qualidade",
        "Liderança em Produção": "Liderança em Produção",
        "Liderança em Projetos": "Liderança em projetos",
        
        # --- Certificados CAE ---
        "Black Belt - Lean Seis Sigma": "Black Belt Lean Seis Sigma",
        "Upgrade Black Belt Lean Six Sigma": "Upgrade Black Belt Lean Six Sigma",
        "DFLSS - Design for Lean Six Sigma": "DFLSS - Design for Lean Six Sigma",
        "Case Six Sigma: Banco": "Case Six Sigma - Banco",
        "Estudo de Caso - Projeto TI": "Estudo de Caso Projeto-TI"
    }
    
    # --- TAGS PARA CADA CERTIFICADO ---
    # As chaves aqui também devem ser os NOMES EXATOS dos arquivos
    tags = {
        "Liderança em operações": '<span class="project-tag">FM2S</span><span class="project-tag">Operações</span>',
        "Liderança em Processos": '<span class="project-tag">FM2S</span><span class="project-tag">Processos</span>',
        "Liderança em qualidade": '<span class="project-tag">FM2S</span><span class="project-tag">Qualidade</span>',
        "Liderança em Produção": '<span class="project-tag">FM2S</span><span class="project-tag">Produção</span>',
        "Liderança em projetos": '<span class="project-tag">FM2S</span><span class="project-tag">Projetos</span>',
        "Black Belt Lean Seis Sigma": '<span class="project-tag">CAE</span><span class="project-tag">Black Belt</span>',
        "Upgrade Black Belt Lean Six Sigma": '<span class="project-tag">CAE</span><span class="project-tag">Black Belt</span>',
        "DFLSS - Design for Lean Six Sigma": '<span class="project-tag">CAE</span><span class="project-tag">DFLSS</span>',
        "Case Six Sigma - Banco": '<span class="project-tag">CAE</span><span class="project-tag">Estudo de Caso</span>',
        "Estudo de Caso Projeto-TI": '<span class="project-tag">CAE</span><span class="project-tag">Estudo de Caso</span>'
    }
    # -------------------------------------

    col1, col2 = st.columns(2)
    
    # Transforma o dicionário em lista para poder usar o índice
    lista_certificados = list(certificados.items())

    # --- ALTURA FIXA ---
    # Defina aqui a altura desejada em pixels para todos os quadros
    FIXED_HEIGHT = 550 

    # Loop para preencher as colunas
    for i, (titulo, nome_arquivo) in enumerate(lista_certificados):
        
        # Define os caminhos completos
        pdf_path = os.path.join(PDF_DIR, f"{nome_arquivo}.pdf")
        img_path = os.path.join(IMG_DIR, f"{nome_arquivo}.png")

        # Alterna entre col1 (par) e col2 (ímpar)
        col = col1 if i % 2 == 0 else col2

        with col:
            # ==========================================================
            # MELHORIA PRINCIPAL: Adicionado o parâmetro 'height'
            # ==========================================================
            with st.container(border=True, height=FIXED_HEIGHT):
                st.markdown(f"### {titulo}")
                
                # Adiciona as tags dinamicamente
                if nome_arquivo in tags:
                    st.markdown(tags[nome_arquivo], unsafe_allow_html=True)

                # --- 1. Exibir a Imagem ---
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.warning(f"⚠️ Imagem não encontrada: {img_path}")
                    st.info(f"Verifique se o arquivo '{nome_arquivo}.png' existe na pasta 'imagens/certificados/'.")
                    st.info("Lembre-se de rodar o script 'gerar_previews.py' após colocar os PDFs na pasta 'certificados/'.")


                # --- 2. Botão de Download do PDF ---
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            f"🔽 Baixar PDF ({nome_arquivo}.pdf)", 
                            f, 
                            file_name=f"{nome_arquivo}.pdf", 
                            use_container_width=True
                        )
                else:
                    st.error(f"Arquivo PDF não encontrado: {pdf_path}")
                    st.info(f"Verifique se o arquivo '{nome_arquivo}.pdf' existe na pasta 'certificados/'.")

                    
                st.write("") # Adiciona um espaço

# ===============================
    # BOTÕES DE NAVEGAÇÃO DE PÁGINA
    # ===============================
    st.write("---") 
    st.markdown("##### Navegar para:")

    # 4 colunas para os botões de navegação
    col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)

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
            on_click=change_page_local, # <--- CORRIGIDO
            args=['Projetos'], 
            use_container_width=True
        )

    with col_nav3:
        st.button(
            "📊 Dashboards", 
            on_click=change_page_local, 
            args=['Dashboards'], 
            use_container_width=True
        )
        
    with col_nav4:
        st.button(
            "📬 Contato", 
            on_click=change_page_local, 
            args=['Contato'], 
            use_container_width=True
        )


# Esta parte é para testar o arquivo isoladamente
if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 'Certificados'
    run()
