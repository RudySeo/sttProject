# app/router/api.py

from fastapi import APIRouter, UploadFile, File
import uuid, os, shutil

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    # 고유한 파일 이름 생성
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")

    # 파일 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "파일 업로드 성공", "file_path": file_path}
