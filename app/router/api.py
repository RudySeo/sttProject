# app/router/api.py

from app.graph.runner.sttSummaryRunner import runGraph
from fastapi import APIRouter, UploadFile, File
import uuid, os, shutil

router = APIRouter()


@router.post("/upload-audio")
async def uploadAudio(file: UploadFile = File(...)):
    """
    오디오 파일을 업로드 받아서 서버에 저장 후
    LangGraph를 통해 STT 및 요약을 수행하는 API입니다.
    """

    # 업로드 파일을 위한 디렉토리 설정
    UPLOAD_DIR = "uploads"
    fileId = str(uuid.uuid4())
    uploadPath = os.path.join(UPLOAD_DIR, f"{fileId}.wav")

    #  업로드 파일을 로컬에 저장
    with open(uploadPath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #  LangGraph를 실행하고 결과 받아오기
    result = await runGraph(uploadPath)

    return {"result": result}
