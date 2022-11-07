from fastapi import WebSocket
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")

bot = ChatBot("Wewy")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


async def processor_response(webSocket: WebSocket):
    while True:
        try:
            message = await webSocket.receive_json()
            bot_response = bot.get_response(message["message"])
            return bot_response.text
        except Exception as e:
            print(e)
            break


