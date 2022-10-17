import fastapi
from .services import chatbot_service
from .models import models

api = fastapi.FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.get("/chatbot/speak")
async def say_hello(body: models.Body):
    chatbot_service.processor_response(body)
    return {"message": f"Your message is: {body.message}"}
