<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> DIO :: BairesDev - Machine Learning Training</span>
</h1>

## Sobre o Projeto

Página desenvolvida para fins didáticos para o desafio - `Agente para Detecção de Vulnerabilidades em Arquiteturas.` do bootcamp **BairesDev - Machine Learning Training** da [Digital Innovation One](https://www.dio.me/). 

## Tecnologias

![PYTHON](https://img.shields.io/badge/PYTHON-000?style=for-the-badge&logo=python&logoColor=30A3DC)
![Yolo](https://img.shields.io/badge/YOLO-000?style=for-the-badge&logo=yolo&logoColor=00FF00)
![Opencv](https://img.shields.io/badge/Opencv-000?style=for-the-badge&logo=opencv&logoColor=0000FF)

## O Desafio

Implementar, documentar e compartilhar um projeto que utilize **Python, FastAPI e Azure OpenAI** para criar uma API capaz de:

* Receber como entrada uma imagem contendo o desenho de arquitetura de uma aplicação;
* Processar essa imagem utilizando técnicas de *prompt engineering*;
* Gerar automaticamente uma análise de ameaças baseada na metodologia **STRIDE** (*Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege*).

⚠️ **Atenção:** Este desafio é flexível!

Você pode optar por implementar a solução completa utilizando Azure OpenAI **ou** documentar em detalhes o que aprendeu sobre os conceitos apresentados, criando um repositório que registre seus estudos, reflexões e exemplos de código.
O mais importante é demonstrar seu entendimento e compartilhar sua jornada de aprendizado!

### Objetivos de Aprendizagem

**Ao concluir este desafio, você será capaz de:**

* Aplicar os conceitos aprendidos em um ambiente prático;
* Documentar processos técnicos de forma clara e estruturada;
* Utilizar o GitHub como ferramenta para compartilhamento de documentação técnica.

### Entrega do Desafio

**Para concluir este desafio, você deverá:**

1. **Assistir a todas as vídeo-aulas**
   Não pule nenhuma etapa! As aulas contêm informações essenciais para o sucesso do seu projeto.

2. **Criar um repositório público no GitHub contendo:**

   * Um arquivo `README.md` detalhado
   * Quaisquer arquivos adicionais que sejam relevantes para documentar sua experiência
   * (Opcional) Capturas de tela relevantes organizadas em uma pasta `/images`

3. **Enviar o link do seu repositório** e uma breve descrição clicando no botão “Entregar Projeto”.

### Recursos Úteis

#### **Documentações Oficiais**

* [**Início Rápido: Criar uma máquina virtual do Windows no Portal do Azure**](https://learn.microsoft.com/pt-br/azure/virtual-machines/windows/quick-create-portal) — Artigo no Microsoft Learning
* [**stride-demo**](https://github.com/digitalinnovationone/stride-demo) — Repositório do projeto

#### **Materiais Complementares sobre GitHub**

* [**GitHub Quick Start**](https://github.com/digitalinnovationone/github-quickstart) — Repositório com link para aulas de Git e GitHub
* [**GitBook: Formação GitHub Certification**](https://aline-antunes.gitbook.io/formacao-fundamentos-github) — Material textual sobre GitHub
* [**Documentação do GitHub**](https://docs.github.com/) — Guia completo para uso do GitHub
* [**GitHub Markdown**](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) — Guia específico para Markdown no GitHub

**OBS**: Com base no material disponibilizado, criarei um agente para analisar prototipagem (design) de site e aplicativos, visando identificar falhas ou itens faltantes nos fluxos desenhados que são importantes para que o time de desenvolvimento possa está alinhado sobre o que o design, e time de produto, deseja que seja implementado.

## Como executar o projeto

### 1. Pré-requisitos

- Python 3.10+
- Node.js (opcional, apenas se quiser servir o front-end com algum servidor local)
- Conta e deployment configurado no Azure OpenAI (veja variáveis de ambiente)

### 2. Clonando o repositório

```bash
# Clone o projeto
 git clone https://github.com/massilva/bootcamps-dio-bairesdev-machine-learning-training-agente-analisador-prototipagem.git analisador
 cd analisador
```

### 3. Configurando o backend (FastAPI)

1. Acesse a pasta do backend:
   ```bash
   cd backend
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Duple o arquivo `env-example` para o nome `.env` com as seguintes variáveis (preencha com seus dados do Azure OpenAI):
   ```env
   AZURE_OPENAI_API_KEY=xxxxxx
   AZURE_OPENAI_ENDPOINT=https://<seu-endpoint>.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2023-05-15
   AZURE_OPENAI_DEPLOYMENT_NAME=<nome-do-deployment>
   ```

5. Execute o backend:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8001
   ```

   O backend estará disponível em http://localhost:8001
