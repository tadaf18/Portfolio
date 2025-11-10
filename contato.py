import streamlit as st

# ===============================
# FUNÇÃO DE AJUDA PARA NAVEGAÇÃO
# ===============================
# Esta função altera o valor no session_state
def change_page_local(page_name):
    st.session_state.page = page_name

def run():
    st.subheader("📬 Contato")

    st.write("Para entrar em contato, por favor, envie um e-mail para: [tarcisio.alves869@gmail.com](mailto:tarcisio.alves869@gmail.com)")
    st.write("Ou me siga nas redes sociais:")

    # LinkedIn
    linkedin_url = "https://www.linkedin.com/in/tarcisioalvesaraujo/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24"/> LinkedIn: @Tarcísio Alves</a>', unsafe_allow_html=True)

    # WhatsApp
    whatsapp_url = "https://wa.me/37998179359"
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="24"/> WhatsApp: (37) 9 9817-9359 </a>', unsafe_allow_html=True)

    # GitHub
    github_url = "https://github.com/tadaf18"
    st.markdown(f'<a href="{github_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="24"/> GitHub: @tadaf18</a>', unsafe_allow_html=True)


    # ===============================
    # BOTÕES DE NAVEGAÇÃO DE PÁGINA
    # ===============================
    st.write("---") # Adiciona um separador visual
    st.markdown("##### Navegar para:")

    # --- ATUALIZAÇÃO AQUI ---
    # Usamos 4 colunas para organizar os botões, incluindo "Certificados"
    col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)

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
            "📊 Dashboards", 
            on_click=change_page_local, 
            args=['Dashboards'], 
            use_container_width=True
        )

    with col_nav4:
        st.button(
            "🎓 Certificados", 
            on_click=change_page_local, 
            args=['Certificados'], 
            use_container_width=True
        )
    # --- FIM DA ATUALIZAÇÃO ---


# Esta parte é para testar o arquivo isoladamente
if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 'Contato'
    run()
