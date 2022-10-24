from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from .services import chatbot_service

api = FastAPI()

origins = [
    "http://localhost:4200"
]

logger = logging.getLogger("uvicorn.info")

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@api.websocket("/test")
async def test(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            logger.info(f"Message received {websocket.application_state}")

            await websocket.send_json(
                await chatbot_service.processor_response(websocket)
            )
    except WebSocketDisconnect:
        logger.error("Disconnect webSocket")


if __name__ == "__main__":
    uvicorn.run("main:api")
