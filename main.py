import streamlit as st
import importlib
import requests
from io import BytesIO
from PIL import Image, ImageDraw

# Função para arredondar a imagem
def make_rounded(image):
    image = image.convert("RGBA")
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    radius = min(width, height) // 2
    center = (width // 2, height // 2)
    draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], fill=255)
    mask = mask.convert("L")
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)
    return rounded_image

# Função para mostrar o conteúdo
# Para rodar no terminal: python -m streamlit run main.py

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

        # Assumindo que o módulo tem a função run()
        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("O módulo não tem uma função 'run' para exibir o conteúdo.")
    else:
        st.write('Página não encontrada.')

# Criando aba de navegação
page = st.sidebar.selectbox(
    'Navegação',
    ['Início', 'Projetos', 'Dashboards', 'Contato']
)

# Exibe o conteúdo da página selecionada ou a página inicial
if page == "Início":
    # Carrega a imagem e aplica a função para torná-la arredondada
    url = 'https://media.licdn.com/dms/image/v2/D4D03AQEI5LWxkyG7YQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1731789177315?e=1763596800&v=beta&t=O2JBLPJ30d0qX45ST4dZ-eonWs85Q25y2ENX3HmMn7g'
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # Arredondar a imagem
    rounded_image = make_rounded(image)

    # Exibe a imagem arredondada
    st.image(rounded_image, caption="Tarcísio Alves", use_column_width=False, width=150)

# criando um resumo

    st.title("Portfólio de Ciência de Dados")
    st.write("""
             Profissional de dados com sólida formação analítica em Engenharia Mecânica e graduação em andamento em Ciência de Dados. Possui experiência prática em Inteligência e Planejamento , destacando-se no desenvolvimento e implementação de modelos para previsão de demanda e na criação de dashboards e relatórios gerenciais em Power BI e Excel para monitoramento de KPIs. Habilidade em análise de dados, SQL, Python e R , combinada com certificação Lean Seis Sigma Black Belt e foco na resolução de problemas e otimização de processos para impulsionar a eficiência operacional através de decisões baseadas em dados.
             """)
else:
    show_pages(page)
