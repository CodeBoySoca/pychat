from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates

login_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@login_router.get('/')
async def login(request: Request):
    return templates.TemplateResponse('login.html', {'request' : request})