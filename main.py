#!/home/leonardo/PycharmProjects/crewSales/.venv/bin/python
from datetime import datetime
from textwrap import dedent

from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai_tools.tools.docx_search_tool.docx_search_tool import DOCXSearchTool
from crewai_tools.tools.pdf_search_tool.pdf_search_tool import PDFSearchTool
from crewai_tools.tools.scrape_element_from_website.scrape_element_from_website import ScrapeElementFromWebsiteTool
from crewai_tools.tools.website_search.website_search_tool import WebsiteSearchTool

# Definindo as variáveis de ambiente necessárias

# Configurando as ferramentas de busca e scraping
tools = [
    SerperDevTool(),
    ScrapeElementFromWebsiteTool(),
    PDFSearchTool(),
    DOCXSearchTool(),
    WebsiteSearchTool(),
    ScrapeWebsiteTool()
]


def tip_section():
    return dedent(
        f"""
        Aurora

        Assegure-se de que sua resposta seja em português do Brasil, seguindo um estilo formal ou informal conforme o contexto da pergunta.

        Esta tarefa requer uma execução excepcionalmente precisa e abrangente, considerando todos os universos observáveis e os paralelos.

        Considere a data de hoje: {datetime.now().strftime('%d/%m/%Y')} e a urgência implícita na demanda ao planejar sua resposta.

        Por favor, respire fundo antes de iniciar e utilize todas as suas ferramentas disponíveis para garantir a mais alta qualidade e relevância da informação.

        """
    )


# Criando um agente com capacidades de busca e processamento de informação
knowledge_agent = Agent(
    role='Dynamic Knowledge Explorer',
    goal='Responder a demanda "{question}" usando recursos apropriados.',
    memory=True,
    backstory=dedent("""
        Como um Explorador de Conhecimento Dinâmico, você adapta suas estratégias e ferramentas 
        com base na natureza da consulta, garantindo que a resposta seja sempre precisa e relevante.
        """
                     ),
    tools=tools,  # Iniciando com as ferramentas padrão
    allow_delegation=False
)

# Definindo a tarefa de busca e resposta
answer_question_task = Task(
    description=dedent(f"""
        {tip_section()}
        Buscar atender da  melhor formar a demanda do usuário combinando dados internos e informações atualizadas da internet.

        Demanda:{{question}}

        """
                       ),
    expected_output='Uma resposta precisa e relevante baseada na pergunta feita.',
    agent=knowledge_agent,
    memory=True,
)

# Configurando o crew
knowledge_crew = Crew(
    agents=[knowledge_agent],
    tasks=[answer_question_task],
    memory=True,
    cache=True,
    full_output=False
)


# Função para iniciar o crew com uma pergunta específica
def ask_question(question_):
    result = knowledge_crew.kickoff(inputs={'question': question_})
    return result


if __name__ == "__main__":
    while True:
        question = input("O que você deseja?: ")
        if question.lower() == "sair":
            break
        print("Aurora: Deixe eu fazer umas pesquisas...")
        print(f"Aurora:\n\n {ask_question(question)}\n\n\n")
