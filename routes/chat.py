from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from socketmanager import manager
from fastapi.responses import HTMLResponse

chat_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@chat_router.get('/chat')
async def chat(request: Request):
    return templates.TemplateResponse('chat.html', {'request' : request})


@chat_router.websocket('/chatroom')
async def chatroom(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f'user says: {data}')
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f' left the chat')

