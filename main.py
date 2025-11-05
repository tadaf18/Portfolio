import streamlit as st
import importlib
import requests
from io import BytesIO
from PIL import Image, ImageDraw

# ===============================
# CONFIGURAÇÕES GERAIS DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Portfólio | Tarcísio Alves",
    page_icon="📊",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS
# ===============================
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .block-container {
            padding-top: 2rem;
            text-align: center;
        }

        .main-title {
            font-size: 2.2em;
            font-weight: 700;
            color: #0A66C2;
            margin-top: 15px;
        }

        .description {
            text-align: justify;
            color: #333333;
            font-size: 1.05em;
            line-height: 1.6em;
            margin-top: 15px;
        }

        .stButton > button {
            background-color: #0A66C2;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.4em;
            font-size: 1em;
            font-weight: 500;
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #004182;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

# ===============================
# FUNÇÃO PARA ARREDONDAR IMAGEM
# ===============================
def make_rounded(image):
    image = image.convert("RGBA")
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    radius = min(width, height) // 2
    center = (width // 2, height // 2)
    draw.ellipse(
        [center[0] - radius, center[1] - radius,
         center[0] + radius, center[1] + radius],
        fill=255
    )
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)
    return rounded_image

# ===============================
# FUNÇÃO PARA EXIBIR PÁGINAS
# ===============================
def show_pages(page_name):
    modules = {
        'Início': 'inicio',
        'Projetos': 'projetos',
        'Dashboards': 'dashboards',
        'Contato': 'contato'
    }

    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)
        if hasattr(module, 'run'):
            module.run()
        else:
            st.warning("O módulo selecionado não possui uma função 'run'.")
    else:
        st.error("Página não encontrada.")

# ===============================
# SIDEBAR - MENU DE NAVEGAÇÃO
# ===============================
st.sidebar.image(
    "https://tse3.mm.bing.net/th/id/OIP.i_cBUKNXRQab9LDeJkjrMQHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
    width=70
)
st.sidebar.title("Navegação")

page = st.sidebar.radio(
    "",
    ['Início', 'Projetos', 'Dashboards', 'Contato'],
    index=0
)

# ===============================
# PÁGINA INICIAL
# ===============================
if page == "Início":
    # Carrega imagem do perfil
    url = 'https://media.licdn.com/dms/image/v2/D4D03AQEI5LWxkyG7YQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1731789177315?e=1763596800&v=beta&t=O2JBLPJ30d0qX45ST4dZ-eonWs85Q25y2ENX3HmMn7g'
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    rounded_image = make_rounded(image)

    # Exibe imagem centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(rounded_image, use_column_width=False, width=180)

    # Título e descrição
    st.markdown('<h1 class="main-title">Portfólio de Ciência de Dados</h1>', unsafe_allow_html=True)
    st.write("---")

    st.markdown("""
    <p class="description">
    Sou <strong>Tarcísio Alves</strong>, profissional de dados com sólida formação analítica em Engenharia Mecânica e
    graduação em andamento em Ciência de Dados. <br><br>
    Tenho experiência prática em Inteligência e Planejamento, com destaque no desenvolvimento e implementação de modelos 
    de previsão de demanda, criação de dashboards interativos e relatórios gerenciais em Power BI e Excel. <br><br>
    Domino ferramentas como <strong>Python, SQL e R</strong>, aliado à certificação <strong>Lean Seis Sigma Black Belt</strong>, 
    com foco na resolução de problemas e otimização de processos para impulsionar a eficiência operacional 
    e tomada de decisão baseada em dados.
    </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # Botões de ação
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.link_button("💼 Ver Projetos", "#Projetos")
    with col_b:
        st.link_button("📊 Dashboards", "#Dashboards")
    with col_c:
        st.link_button("📬 Contato", "#Contato")

    # ===============================
    # CURRÍCULO - BOTÃO PARA DOWNLOAD LOCAL
    # ===============================
    st.write("---")
    st.markdown("### 📘 Currículo")

    try:
        with open("curriculo.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Baixar Currículo (PDF)",
            data=PDFbyte,
            file_name="Tarcisio_Alves_Curriculo.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.warning("⚠️ O arquivo 'curriculo.pdf' não foi encontrado na pasta do projeto.")

else:
    show_pages(page)
