import streamlit as st

def run():
    st.subheader("Contato")

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

if __name__ == "__main__":
    run()