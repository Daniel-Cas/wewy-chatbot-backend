from fastapi import WebSocket
from time import sleep



async def processor_response(webSocket: WebSocket):
    message = await webSocket.receive_json()
    sleep(1)
    return f"Hola, ¿que tal? Lamento decirte esto, pero aún no estoy disponible :c"
