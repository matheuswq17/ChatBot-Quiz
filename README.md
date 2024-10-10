# Documentação Completa do Chatbot de WhatsApp

## Índice
1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Configuração Inicial](#configuração-inicial)
4. [Funcionalidades](#funcionalidades)
5. [Estrutura do Código](#estrutura-do-código)
6. [Como Executar o Chatbot](#como-executar-o-chatbot)
7. [Testes e Validação](#testes-e-validação)
8. [Melhorias Futuras](#melhorias-futuras)

## Introdução
Este projeto é um chatbot de WhatsApp desenvolvido com Flask e utilizando a API do WhatsApp Cloud da Meta. O chatbot foi criado por Matheus Xavier e é especializado em quizzes de diferentes temas, como cultura pop, super-heróis, história dos videogames, e tecnologias e invenções ao longo do tempo. Este documento descreve os requisitos, como configurar e executar o chatbot, suas funcionalidades, e apresenta possibilidades de futuras melhorias.

## Requisitos
Para executar este projeto, você precisará dos seguintes itens:

- Python 3.7 ou superior
- Flask
- requests (biblioteca para chamadas HTTP)
- Ngrok (para expor o servidor Flask a uma URL externa)
- Conta de desenvolvedor no Meta para acessar a API do WhatsApp Cloud
- Um número de teste do WhatsApp configurado na API do WhatsApp Cloud

## Configuração Inicial
**Requests**: Uma biblioteca para fazer requisições HTTP, essencial para comunicar-se com a API do WhatsApp Cloud. Instale com:
    ```bash
    pip install requests

**Ngrok**: Ferramenta para expor o servidor Flask a uma URL pública, permitindo que o webhook da Meta consiga se conectar ao seu servidor local. Você pode baixar o Ngrok aqui. Depois de baixar, descompacte e adicione ao PATH do sistema.

**Conta de desenvolvedor no Meta**: Para acessar a API do WhatsApp Cloud e obter tokens de acesso. Você precisará configurar um aplicativo no painel de desenvolvedor da Meta e gerar o token de acesso.

**Número de teste do WhatsApp**: Configurado na API do WhatsApp Cloud para poder testar o chatbot. Este número será usado para enviar e receber mensagens durante o desenvolvimento

1. **Clone o Repositório**: Clone o projeto em sua máquina local.
   ```bash
   git clone <https://github.com/matheuswq17/ChatBot-Quiz>
   cd whatsapp_chatbot
   
2. **Crie e Ative um Ambiente Virtual**:
   ```bash
    python -m venv venv
    # Ativar no Windows
    .\venv\Scripts\activate
    # Ativar no Linux/macOS
    source venv/bin/activate

3. **Instale as Dependências**:
   ```bash
    pip install -r requirements.txt

4. **Configuração do Token de Acesso**: Atualize o valor da variável ACCESS_TOKEN no código para o token de acesso obtido do painel de desenvolvedor da Meta.

5. **Ngrok**: Instale o Ngrok e inicie o tunelamento para a porta 5000:
   ```bash
    ngrok http 5000
Utilize a URL gerada pelo Ngrok para configurar o webhook no painel da Meta. Lembre-se de adicionar /webhook ao final da URL do Ngrok ao configurá-lo no Meta (ex.: https://seu-ngrok-url/webhook).

## Funcionalidades
**Menu Principal**
Quando o usuário envia uma mensagem inicial como "menu" ou "iniciar", o chatbot envia uma mensagem de boas-vindas e apresenta quatro opções de quiz:
    Quiz de Cultura Pop ✨
    Quiz de Super-Heróis 🦸‍♂️🦸‍♀️
    Quiz da História dos Videogames 🎮📜
    Quiz de Tecnologias e Invenções ao Longo do Tempo 💡🔧

**Quiz de Perguntas**
    O chatbot apresenta ao usuário uma série de perguntas de múltipla escolha com temas diferentes. Cada quiz contém 5 perguntas.
    A cada resposta correta ou incorreta, o chatbot envia uma mensagem personalizada, incluindo emojis para tornar a interação mais divertida.
    Ao final do quiz, o usuário é questionado se deseja retornar ao menu principal ou encerrar a conversa.

## Estrutura do Código
**Principais Componentes do Código**
    Flask: Utilizado para criar um servidor web que recebe e responde às requisições enviadas pelo WhatsApp.
    Ngrok: Utilizado para expor o servidor local a uma URL pública, permitindo que o webhook da API do WhatsApp consiga se comunicar com o servidor.
    requests: Utilizado para enviar mensagens de volta ao WhatsApp, realizando requisições HTTP para a API do WhatsApp Cloud.

**Funções Importantes**
    verify_webhook(): Responsável por verificar a URL do webhook quando configurada no painel da Meta.
    receive_message(): Manipula as mensagens recebidas e processa de acordo com o contexto do usuário.
    enviar_proxima_pergunta(): Envia a próxima pergunta do quiz.
    send_message(): Função genérica para enviar mensagens para o usuário via API do WhatsApp.
    menu_principal(): Gera a mensagem do menu principal para o usuário.