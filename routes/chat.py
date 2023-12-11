from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates

chat_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@chat_router.get('/chat/')
async def chat(request: Request):
    return templates.TemplateResponse('chat.html', {'request' : request})