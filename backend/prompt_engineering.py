
class PromptEngineer:
    @staticmethod
    def build_prompt_analize_diagram(application_type: str, description: str):
        return f"""Aja como um especialista em engenharia de software e designer de produtos de software com mais de 20 anos de experiência 
        utilizando uma metodologia baseada em grandes autores Ian Sommerville, Marco Tulio Valente e Roger Pressman.
        Alinhada com as 10 heurísticas de Jakob Nielsen.

        Sua tarefa é analisar o resumo do código, o conteúdo do README e a descrição da aplicação fornecidos para produzir uma lista de 
        pontos específicos para melhoria do prototipagem da aplicação.

        Presta atenção na descrição da aplicação e nos detalhes técnicos fornecidos.

        Analise as telas de forma individual e forma de um fluxo (processo) a ser realizado pelo usuário.
        Liste os pontos que podem ser melhorados, exemplo de falhas, não exaustiva:
        - Na tela de login, está faltando mostrar a mensagem de erro quando o login falhar.
        - Na tela de login, não há o link para a página de recuperação de senha.
        - Não é possível saber qual é a primeira página, que normalmente é onboarding ou tela de login.
        - Na tela inicial, está faltando mostrar o caso da lista está vázia, além disso, não há um tratamento para caso de erro, nem nesta página, nem no projeto em geral.
        - Não respeita a heurística 10 - Usabilidade e acessibilidade.

        Utilize uma resposta formatada em JSON com as chaves "resume" - contendo o entendimento geral da aplicação, a partir da analise do diagrama em contapartida
        a descrição fornecida pelo usuário, "positives" - lista (array) de pontos positivos de destaque com no máximo 5 itens, e "negatives" - lista (array) de pontos a serem melhorados
        com no máximo 10 itens.

        Não forneça recomendações de segurança genéricas — foque apenas no que ajudaria a criar um modelo de prototipagem mais eficiente e que respeite os pré-requisitos necessários para 
        serem alinhados e disponibilizados para o time de desenvolvimento.

        TIPO DE APLICAÇÃO: {application_type}
        RESUMO DE CÓDIGO, CONTEÚDO DO README E DESCRIÇÃO DA APLICAÇÃO: {description}

        Exemplo de formato esperado em JSON:

        {{
        "resume": "Uma aplicação para compartilhamento de locais (restaurantes, bares, praças, ...), interessantes para visitantes de uma cidade.",
        "positives": [
            "A aplicação possui uma interface simples e intuitiva para o usuário.",
            "Tem área para configuração de tamanho da fonte, ideal para pessoas com baixa visão e idosos"
        ],
        "negatives": [
            "Na tela de login, está faltando mostrar a mensagem de erro quando o login falhar.",
            "A lista de lugares não tem a tela da listagem sem itens",
            "Muita informação na tela inicial, sem indicativo de quantos itens devem aparecer por pagina",
            // ... mais sugestões para melhorar o modelo de ameaças
        ]
        }}"""
