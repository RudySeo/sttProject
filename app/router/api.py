# app/router/api.py

from fastapi import APIRouter, UploadFile, File, HTTPException
import uuid, os, shutil
from app.service.sttService import transcribe_audio_with_api, validate_api_key

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    # API 키 유효성 확인
    if not validate_api_key():
        raise HTTPException(
            status_code=401, detail="유효하지 않은 OpenAI API 키입니다."
        )

    # 고유한 파일명 생성
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")

    # 파일 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Whisper API로 STT 처리
    try:
        text = transcribe_audio_with_api(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"STT 처리 실패: {e}")

    return {"message": "STT 성공", "text": text}
