from fastapi import WebSocket


async def processor_response(webSocket: WebSocket):
    message = await webSocket.receive_json()
    return f"Hola, ¿que tal? Lamento decirte esto, pero aún no estoy disponible :c"
