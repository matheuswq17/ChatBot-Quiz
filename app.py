from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

VERIFY_TOKEN = "minha_senha_secreta"
ACCESS_TOKEN = "EAAMPZCYn5McIBO2r1oIenrCQ8GjDv8g2yzYN059mX23dTKZABUayJuynfDiSErB4sZAAJijZA8rK50Tb0T85rZAi6Lc2UdBhZB4qYh7IHcGVgGc4zI6d0wu3qpheyX6Q2fdZBgpwwte7EdNQForBX5nj9R7g7SYsnNwF5XR7fLAvzN0m0tw13ynDBs2hVx7R9mJiQZDZD"

# Perguntas do quiz de cultura pop
quiz_perguntas_cultura_pop = [
    {
        "pergunta": "Qual é o nome do personagem principal da série 'Breaking Bad'?",
        "opcoes": ["1. Jesse Pinkman", "2. Walter White", "3. Saul Goodman", "4. Hank Schrader"],
        "resposta_correta": "2",
        "emojis": "🎬👨‍🔬💊"
    },
    {
        "pergunta": "Qual é o nome da princesa no filme 'Cinderela'?",
        "opcoes": ["1. Ariel", "2. Bela", "3. Cinderela", "4. Aurora"],
        "resposta_correta": "3",
        "emojis": "👸✨🎀"
    },
    {
        "pergunta": "Em qual filme encontramos o personagem Jack Sparrow?",
        "opcoes": ["1. Harry Potter", "2. Piratas do Caribe", "3. Indiana Jones", "4. O Senhor dos Anéis"],
        "resposta_correta": "2",
        "emojis": "🏴‍☠️⚓️🌊"
    },
    {
        "pergunta": "Quem interpreta o Homem de Ferro no universo da Marvel?",
        "opcoes": ["1. Chris Evans", "2. Robert Downey Jr.", "3. Mark Ruffalo", "4. Chris Hemsworth"],
        "resposta_correta": "2",
        "emojis": "🤖🧠💥"
    },
    {
        "pergunta": "Qual é a casa de Harry Potter conhecida por sua coragem?",
        "opcoes": ["1. Sonserina", "2. Corvinal", "3. Grifinória", "4. Lufa-Lufa"],
        "resposta_correta": "3",
        "emojis": "🦁🏰⚡"
    }
]

# Perguntas do quiz de super-heróis
quiz_perguntas_super_herois = [
    {
        "pergunta": "Qual é o alter ego do Superman?",
        "opcoes": ["1. Bruce Wayne", "2. Clark Kent", "3. Peter Parker", "4. Tony Stark"],
        "resposta_correta": "2",
        "emojis": "🦸‍♂️🦸‍♀️🌍"
    },
    {
        "pergunta": "Qual super-herói é conhecido como o 'Cavaleiro das Trevas'?",
        "opcoes": ["1. Batman", "2. Superman", "3. Homem-Aranha", "4. Flash"],
        "resposta_correta": "1",
        "emojis": "🦇🌃🖤"
    },
    {
        "pergunta": "Qual é o nome verdadeiro do Homem-Aranha?",
        "opcoes": ["1. Tony Stark", "2. Steve Rogers", "3. Peter Parker", "4. Bruce Banner"],
        "resposta_correta": "3",
        "emojis": "🕷️🕸️🏙️"
    },
    {
        "pergunta": "Qual super-heroína é uma amazona e usa um laço da verdade?",
        "opcoes": ["1. Viúva Negra", "2. Mulher-Maravilha", "3. Feiticeira Escarlate", "4. Capitã Marvel"],
        "resposta_correta": "2",
        "emojis": "👑🗡️💫"
    },
    {
        "pergunta": "Qual super-herói tem um martelo mágico chamado Mjölnir?",
        "opcoes": ["1. Thor", "2. Loki", "3. Capitão América", "4. Hulk"],
        "resposta_correta": "1",
        "emojis": "⚡🔨🌩️"
    }
]

# Perguntas do quiz de História dos videogames
quiz_perguntas_videogames = [
    {
        "pergunta": "Qual foi o primeiro console de videogame lançado comercialmente?",
        "opcoes": ["1. Atari 2600", "2. Magnavox Odyssey", "3. NES", "4. Sega Genesis"],
        "resposta_correta": "2",
        "emojis": "🎮📜🕹️"
    },
    {
        "pergunta": "Qual empresa criou o jogo 'Super Mario'?",
        "opcoes": ["1. Sega", "2. Atari", "3. Nintendo", "4. Sony"],
        "resposta_correta": "3",
        "emojis": "🍄👨‍🎤⭐"
    },
    {
        "pergunta": "Qual console popularizou o uso de CDs para jogos?",
        "opcoes": ["1. PlayStation", "2. Nintendo 64", "3. Sega Saturn", "4. Xbox"],
        "resposta_correta": "1",
        "emojis": "💿🎮📀"
    },
    {
        "pergunta": "Qual franquia de jogos é conhecida pela frase 'Hadouken'?",
        "opcoes": ["1. Mortal Kombat", "2. Street Fighter", "3. Tekken", "4. King of Fighters"],
        "resposta_correta": "2",
        "emojis": "👊🔥🎯"
    },
    {
        "pergunta": "Qual jogo é considerado o primeiro RPG eletrônico?",
        "opcoes": ["1. Final Fantasy", "2. Dragon Quest", "3. The Legend of Zelda", "4. Ultima"],
        "resposta_correta": "4",
        "emojis": "🛡️🗡️👾"
    }
]

# Perguntas do quiz de Tecnologias e invenções ao longo do tempo
quiz_perguntas_tecnologia_invencoes = [
    {
        "pergunta": "Quem inventou a lâmpada elétrica?",
        "opcoes": ["1. Nikola Tesla", "2. Thomas Edison", "3. Alexander Graham Bell", "4. Benjamin Franklin"],
        "resposta_correta": "2",
        "emojis": "💡🔧🔋"
    },
    {
        "pergunta": "Qual foi o primeiro meio de transporte motorizado?",
        "opcoes": ["1. Avião", "2. Bicicleta", "3. Automóvel", "4. Trem a vapor"],
        "resposta_correta": "3",
        "emojis": "🚗🛤️🚂"
    },
    {
        "pergunta": "Quem é o inventor do telefone?",
        "opcoes": ["1. Thomas Edison", "2. Alexander Graham Bell", "3. Nikola Tesla", "4. Guglielmo Marconi"],
        "resposta_correta": "2",
        "emojis": "📞🔊📠"
    },
    {
        "pergunta": "Qual foi o primeiro navegador da internet amplamente utilizado?",
        "opcoes": ["1. Internet Explorer", "2. Netscape Navigator", "3. Mozilla Firefox", "4. Google Chrome"],
        "resposta_correta": "2",
        "emojis": "🌐💻📁"
    },
    {
        "pergunta": "Quem inventou o avião?",
        "opcoes": ["1. Irmãos Wright", "2. Santos Dumont", "3. Leonardo da Vinci", "4. Charles Lindbergh"],
        "resposta_correta": "1",
        "emojis": "✈️🛠️🌍"
    }
]

# Variável para armazenar o estado dos usuários (por exemplo, qual pergunta do quiz estão)
estado_usuarios = {}

# Respostas para acertos e erros
mensagens_acerto = [
    "Resposta correta! 🎉",
    "Mandou bem! 👏",
    "Você acertou! 🤩",
    "Boa! Você está arrasando! 💪",
    "Incrível! Continue assim! 🌟"
]

mensagens_erro = [
    "Resposta incorreta. 😢",
    "Ah, quase! Tente a próxima! 🙃",
    "Não foi dessa vez, mas continue tentando! 💪",
    "Errou, mas não desanime! ✨",
    "Poxa, não foi dessa vez. Vamos para a próxima! 😅"
]

# Endpoint para verificação do Webhook
@app.route('/webhook', methods=['GET'])
def verify_webhook():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return str(challenge)
    return "Token de verificação inválido", 403

# Endpoint para receber mensagens
@app.route('/webhook', methods=['POST'])
def receive_message():
    data = request.get_json()
    print("Dados recebidos:", data)

    if 'entry' in data and len(data['entry']) > 0:
        changes = data['entry'][0]['changes'][0]['value']
        if 'messages' in changes:
            message = changes['messages'][0]

            # Verifica se a mensagem é do tipo "text" antes de continuar
            if message['type'] == 'text':
                phone_number = message['from']
                message_text = message.get('text', {}).get('body', '').strip().lower()

                # Lógica do menu de opções
                if phone_number in estado_usuarios:
                    estado = estado_usuarios[phone_number]

                    # Verificação do estado do quiz ou pós-quiz
                    if "pergunta_atual" in estado:
                        # Usuário está no meio do quiz
                        if message_text == "0":
                            send_message(phone_number, menu_principal())
                            del estado_usuarios[phone_number]
                        else:
                            pergunta_atual = estado["pergunta_atual"]
                            quiz = estado["quiz"]

                            if pergunta_atual < len(quiz):
                                pergunta = quiz[pergunta_atual]

                                # Verificar a resposta do usuário
                                if message_text == pergunta["resposta_correta"]:
                                    estado_usuarios[phone_number]["pontuacao"] += 1
                                    send_message(phone_number, random.choice(mensagens_acerto))
                                else:
                                    send_message(phone_number, random.choice(mensagens_erro))

                                # Enviar próxima pergunta
                                estado_usuarios[phone_number]["pergunta_atual"] += 1
                                enviar_proxima_pergunta(phone_number)
                    elif "menu_pos_quiz" in estado:
                        # Usuário está no menu pós-quiz
                        if message_text == "1":
                            send_message(phone_number, menu_principal())
                            del estado_usuarios[phone_number]
                        elif message_text == "2":
                            send_message(phone_number, "Obrigado por participar! Se precisar de algo mais, estou à disposição. 👋")
                            del estado_usuarios[phone_number]
                        else:
                            send_message(phone_number, "Opção inválida. Digite *1* para voltar ao menu ou *2* para encerrar a conversa.")
                else:
                    # Usuário ainda não está em um quiz ou menu
                    if message_text in ["menu", "iniciar"]:
                        send_message(phone_number, menu_principal())

                    elif message_text == "1":
                        # Iniciar o quiz de cultura pop
                        estado_usuarios[phone_number] = {"pergunta_atual": 0, "pontuacao": 0, "quiz": quiz_perguntas_cultura_pop}
                        enviar_proxima_pergunta(phone_number)

                    elif message_text == "2":
                        # Iniciar o quiz de super-heróis
                        estado_usuarios[phone_number] = {"pergunta_atual": 0, "pontuacao": 0, "quiz": quiz_perguntas_super_herois}
                        enviar_proxima_pergunta(phone_number)

                    elif message_text == "3":
                        # Iniciar o quiz de História dos videogames
                        estado_usuarios[phone_number] = {"pergunta_atual": 0, "pontuacao": 0, "quiz": quiz_perguntas_videogames}
                        enviar_proxima_pergunta(phone_number)

                    elif message_text == "4":
                        # Iniciar o quiz de Tecnologias e invenções
                        estado_usuarios[phone_number] = {"pergunta_atual": 0, "pontuacao": 0, "quiz": quiz_perguntas_tecnologia_invencoes}
                        enviar_proxima_pergunta(phone_number)

                    else:
                        send_message(phone_number, "🤖Desculpe, não entendi sua mensagem. Digite 'menu' para ver as opções🤖")

    return "Evento Recebido", 200

# Função para enviar pergunta do quiz
def enviar_proxima_pergunta(phone_number):
    estado = estado_usuarios.get(phone_number, {})
    pergunta_atual = estado.get("pergunta_atual", 0)
    quiz = estado.get("quiz", [])

    if pergunta_atual < len(quiz):
        pergunta = quiz[pergunta_atual]
        opcoes = "\n".join(pergunta["opcoes"])
        send_message(phone_number, f"*Pergunta {pergunta_atual + 1}* {pergunta['emojis']}\n{pergunta['pergunta']}\n\n{opcoes}\n\nDigite 0 para retornar ao menu")
    else:
        pontuacao = estado.get("pontuacao", 0)
        send_message(phone_number, f"Fim do quiz! 🎉 Você acertou {pontuacao} de {len(quiz)} perguntas.\n\nGostaria de voltar ao menu ou encerrar o papo?\n*1.* Voltar ao menu\n*2.* Encerrar conversa")
        estado_usuarios[phone_number] = {"menu_pos_quiz": True}

# Função para enviar mensagem usando a API do WhatsApp
def send_message(to, message):
    url = "https://graph.facebook.com/v20.0/487028274484305/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code, response.json())

# Função para gerar o menu principal com uma introdução personalizada
def menu_principal():
    return (
        "Olá! Eu sou um chatbot especializado em quizzes, criado por Matheus Xavier. 🤖\n"
        "Aqui você pode se divertir respondendo perguntas de cultura pop, super-heróis, sobre a história dos videogames, ou sobre tecnologias e invenções ao longo do tempo. 📚✨\n\n"
        "*Escolha uma das opções:*\n"
        "*1.* Fazer um quiz de cultura pop 🎉\n"
        "*2.* Fazer um quiz de super-heróis 🦸‍♂️🦸‍♀️\n"
        "*3.* Fazer um quiz sobre a história dos videogames 🎮📜\n"
        "*4.* Fazer um quiz sobre tecnologias e invenções ao longo do tempo 💡🔧"
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)