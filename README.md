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

1. **Clone o Repositório**: Clone o projeto em sua máquina local.
   ```bash
   git clone <URL-do-repositório>
   cd whatsapp_chatbot
