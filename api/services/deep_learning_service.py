from fastapi import WebSocket
from time import sleep
import numpy as np
import json
import re
import tensorflow as tf
import warnings
import random
import spacy

nlp = spacy.load('en_core_web_sm')

warnings.filterwarnings('ignore')

with open('job_intents.json', 'rb') as file:
    data = json.load(file)


def pre_processing(line):
    line = re.sub(r'[a-zA-Z.?!\']', ' ', line)
    line = re.sub(r'[ ]+', ' ', line)
    return line



async def processor_response(webSocket: WebSocket):
    message = await webSocket.receive_json()
    sleep(1)
    return f"Hola, ¿que tal? Lamento decirte esto, pero aún no estoy disponible :c"
