import openai
import os
from dotenv import load_dotenv

# .env 파일의 변수들을 환경변수로 로드
load_dotenv()

# 환경변수에서 API 키를 가져옴
openai.api_key = os.getenv("OPENAI_API_KEY")


def validate_api_key() -> bool:
    """
    API 키가 유효한지 테스트 요청으로 확인
    """
    try:
        openai.Model.list()  # 간단한 인증 요청
        return True
    except Exception as e:
        print(f"[ERROR] OpenAI 인증 실패: {e}")
        return False


def transcribe_audio_with_api(file_path: str) -> str:
    """
    OpenAI Whisper API로 음성 파일을 텍스트로 변환
    "rb"는 바이너리 읽기 모드(read binary)
    """
    with open(file_path, "rb") as audio_file:
        result = openai.Audio.transcribe("whisper-1", audio_file)

        return {
            "text": result.get("text"),
            "language": result.get("language"),
            "duration": result.get("duration"),
        }
