# app/main.py

from fastapi import FastAPI
from app.router.api import router  # 라우터 불러오기

app = FastAPI()

# 라우터 등록
app.include_router(router)
