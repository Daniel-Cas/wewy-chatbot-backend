from fastapi import WebSocket


async def processor_response(webSocket: WebSocket):
    message = await webSocket.receive_json()
    return f"Your message is: {message}"
