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

## Como Executar o Chatbot
1. **Ative o Ambiente Virtual**:
    ```bash
    # Windows
    .\venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate

2. **Execute o Servidor Flask**:
    ```bash
    python app.py

3. **Ngrok:** Em uma nova janela de terminal, execute o comando do Ngrok:
    ```bash
    ngrok http 5000

Use a URL fornecida pelo Ngrok para configurar o webhook no Meta. Não esqueça de adicionar /webhook ao final da URL.

4. **Teste no WhatsApp**: Utilize o número de teste configurado para enviar mensagens para o bot e testar as funcionalidades.

## Testes e Validação
**Token de Verificação**: Verifique se o VERIFY_TOKEN corresponde ao valor usado na configuração do webhook no Meta.
**Logs do Flask**: Sempre monitore os logs do terminal onde o Flask está rodando para diagnosticar problemas.
**Ngrok**: Certifique-se de que o ngrok está ativo e o link é válido. Se precisar reiniciar o ngrok, atualize o webhook com a nova URL.

## Erros Comuns e Soluções
1. **Erro 403 - Forbidden ao Verificar o Webhook**:
    Certifique-se de que o VERIFY_TOKEN no código corresponde exatamente ao token fornecido na configuração do webhook.

2. **Ngrok não Conecta**:
    Verifique se o ngrok está em execução. Se precisar reiniciar, atualize o link do webhook no painel da Meta.

3. **Token Expirado**:
    Caso o token de acesso expire, obtenha um novo no painel de desenvolvedor da Meta e substitua no código.

## Melhorias Futuras
1. **Persistência de Dados**: Implementar uma base de dados para salvar os estados dos usuários, como progresso dos quizzes, pontuações, e histórico de interações.
2. **Melhorias na Interface**: Adicionar mais tipos de mensagens, como imagens ou áudios, para tornar a interação mais envolvente.
3. **Mais Quizzes**: Criar novos quizzes sobre diferentes temas para atrair diferentes tipos de público.
4. **Automação do Setup**: Criar scripts de automação para facilitar a configuração e execução do chatbot para novos desenvolvedores.

## Guia para Contribuidores
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor siga as etapas abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua feature ou correção.
    ```bash
    git checkout -b minha-nova-feature
3. Faça commit das suas alterações.
    ```bash
    git commit -m "Adicionando uma nova feature"

4. Faça o push para a branch.
    ```bash
    git push origin minha-nova-feature
5. Abra uma Pull Request no GitHub.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.