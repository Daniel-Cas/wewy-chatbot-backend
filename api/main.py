from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

@app.websocket("/test")
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        request = await websocket.receive_json()
        message = request["message"]
        await websocket.send_json({
            "message": f" This is your message: {message}"
        })

if __name__ == "__main__":
    uvicorn.run("main:app")
