from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.chat import chat_router
from routes.login import login_router
from socketmanager import manager

import hypercorn


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(chat_router)
app.include_router(login_router)