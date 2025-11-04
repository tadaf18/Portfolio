import streamlit as st
import importlib

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

# criando um resumo

if page == 'Início':

    st.title("Portfólio de Ciência de Dados")
    st.write("""
             Profissional de dados com sólida formação analítica em Engenharia Mecânica e graduação em andamento em Ciência de Dados. Possui experiência prática em Inteligência e Planejamento , destacando-se no desenvolvimento e implementação de modelos para previsão de demanda e na criação de dashboards e relatórios gerenciais em Power BI e Excel para monitoramento de KPIs. Habilidade em análise de dados, SQL, Python e R , combinada com certificação Lean Seis Sigma Black Belt e foco na resolução de problemas e otimização de processos para impulsionar a eficiência operacional através de decisões baseadas em dados.
             """)
else:
    show_pages(page)